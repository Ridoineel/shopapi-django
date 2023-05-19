from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from boutique.models import Category
from .product_serializer import ProductSerializer

class CategoryBaseSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = ("id", "name", "description", "date_created", "date_updated")

class CategoryListSerializer(CategoryBaseSerializer):
	class Meta:
		model = Category
		fields = ("id", "name", "description", "date_created", "date_updated")

	def validate_name(self, value):
		value = value.upper()

		if Category.objects.filter(name__iexact=value).exists():
			raise serializers.ValidationError("Cette categorie existe déjà")

		return value

class CategoryUpdateSerializer(CategoryBaseSerializer):
	def validate_name(self, value):
		value = value.upper()

		if self.instance.name.upper() != value and Category.objects.filter(name__iexact=value).exists():
			raise serializers.ValidationError("Cette categorie existe déjà")

		return value

class CategoryDetailSerializer(ModelSerializer):
	products = SerializerMethodField()

	class Meta:
		model = Category
		fields = ("id", "name", "date_created", "date_updated", "products")

	def get_products(self, instance):
		queryset = instance.products.filter(active=True)

		serializer = ProductSerializer(queryset, many=True)

		return serializer.data