from django.db import transaction
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
import firebase_admin
from firebase_admin import storage
from testsn.settings import storage_client
from boutique.models import Product
from boutique.serializers import ProductSerializer, ProductCreateSerializer, ProductListSerializer, ProductUpdateSerializer
from boutique.permissions import IsAdminAuthenticated
from boutique.views.base import BaseViewSet
from boutique.utils.functions import compressImage
import time


class ProductBaseViewSet(BaseViewSet):
	serializer_class = ProductSerializer
	detail_serializer_class = ProductListSerializer
	create_serializer_class = ProductCreateSerializer
	list_serializer_class = ProductListSerializer

	def get_queryset(self):
		queryset = Product.objects.filter(active=True)

		category_id = self.request.GET.get("category_id")
		price = self.request.GET.get("price")
		name = self.request.GET.get("name")

		if category_id:
			queryset = queryset.filter(category_id=category_id)

		if price:
			queryset = queryset.filter(price=price)

		if name:
			queryset = queryset.filter(name__iexact=name)

		return queryset

class ProductViewSet(ProductBaseViewSet, ReadOnlyModelViewSet):
	pass

class AdminProductViewSet(ProductBaseViewSet, BaseViewSet, ModelViewSet):
	update_serializer_class = ProductUpdateSerializer
	permission_classes = [IsAdminAuthenticated]

	def get_queryset(self):
		return Product.objects.all()

	def perform_create(self, serializer: ProductCreateSerializer):
		image_file = serializer.validated_data.get('image')

		if image_file:
			image_file_extension = image_file.content_type.split("/")[1]
			
			# compress image file (get bytes)
			compressed_image = compressImage(image_file, format=image_file_extension.upper())

			# image file name
			product_name = serializer.validated_data['name'][:30]
			product_name = product_name.replace(" ", "")
			image_file_name = f"{product_name.lower()}_{int(time.time())}.{image_file_extension}"

			blob = storage_client.blob(image_file_name)
			
			blob.upload_from_file(compressed_image, content_type=image_file.content_type)
			
			# definition des droits d'accès
			# public sur l'image
			blob.make_public()

			# Récupération de l'URL de téléchargement de l'image
			image_url = blob.public_url

			# exclure {image}
			# pour eviter la sauvegarde local
			serializer.validated_data.pop("image")
			
			# Enregistrement de l'URL de l'image dans l'objet serializer
			serializer.save(image_url=image_url)
		else:
			serializer.save()
	
	@transaction.atomic
	def perform_update(self, serializer: ProductUpdateSerializer):
		image_url = None

		if serializer.validated_data.get('image'):
			product = Product.objects.get(name=serializer.validated_data.get('name'))
			image_url = product.image_url

		self.perform_create(serializer)

		if image_url:
			# delete old image on firebase
			self._deleteImageOnFirebase(image_url)
	
	def perform_destroy(self, serializer):
		self._deleteImageOnFirebase(serializer.image_url)

		# delete product
		serializer.delete()
	
	def _deleteImageOnFirebase(self, image_url):
		# delete product image on firebase

		if not image_url:
			return

		try:
			image_file_name = image_url.split("/")[-1]
			
			file_ref = storage_client.blob(image_file_name)
			file_ref.delete()	
		except:
			pass
