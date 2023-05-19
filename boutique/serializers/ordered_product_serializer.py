from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from boutique.models import OrderedProduct
from .product_serializer import ProductSerializer

class OrderedProductSerializer(ModelSerializer):
	product = serializers.SerializerMethodField()

	class Meta:
		model = OrderedProduct
		fields = ("id", "product", "quantity")
	
	def get_product(self, instance):
		queryset = instance.product

		serializer  = ProductSerializer(queryset)

		return serializer.data