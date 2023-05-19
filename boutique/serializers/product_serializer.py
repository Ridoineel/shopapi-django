from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from boutique.models import Product, Category
from django.conf import settings

class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ("id", "name", "image_url", "category", "price", "description", "currency", "date_created", "date_updated")

class ProductListSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ("id", "name", "image_url", "category", "price", "description", "currency", "date_created", "date_updated")

class ProductWriteSerializer(ModelSerializer):
	image = serializers.ImageField(write_only=True, required=False)
	image_url = serializers.URLField(read_only=True)

	class Meta:
		model = Product
		fields = ("id", "name", "image", "image_url", "category", "price", "description", "currency", "date_created", "date_updated")

	def validate_category(self, value):
		if not Category.objects.filter(name__iexact=value):
			raise serializers.ValidationError("La caegorie n'existe pas")

		return value

	def validate_price(self, value):
		if value <= 0:
			raise serializers.ValidationError("Le prix est invalide")

		return value
	
	

class ProductCreateSerializer(ProductWriteSerializer):
	def validate_name(self, value):
		value = value.upper()

		if Product.objects.filter(name__iexact=value).exists():
			raise serializers.ValidationError("Ce produit existe déjà")

		return value

class ProductUpdateSerializer(ProductWriteSerializer):
	def validate_name(self, value):
		value = value.upper()

		if self.instance.name.upper() != value and Product.objects.filter(name__iexact=value).exists():
			raise serializers.ValidationError("Ce produit existe déjà")

		return value

		
