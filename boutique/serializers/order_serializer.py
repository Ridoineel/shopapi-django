from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from boutique.models import Order, Product
from .ordered_product_serializer import OrderedProductSerializer

class OrderBaseSerializer(ModelSerializer):
	class Meta:
		model = Order
		fields = ("id", "client", "status", "date_created", "date_updated")

class OrderListSerializer(OrderBaseSerializer):
	pass

class OrderDetailSerializer(ModelSerializer):
	products = SerializerMethodField()

	class Meta:
		model = Order
		fields = ("id", "client", "status", "products", "date_created", "date_updated")

	def get_products(self, instance):
		queryset = instance.products

		serializer = OrderedProductSerializer(queryset, many=True)

		return serializer.data

class OrderWriteSerializer(ModelSerializer):
	orderedProducts = serializers.ListField(write_only=True)

	# orderedProducts = Product()

	class Meta:
		model = Order
		fields = ("id", "client", "orderedProducts", "status", "date_created", "date_updated")

		extra_kwargs = {
			"id": {"read_only": True},
			"client": {"read_only": True}
		}

	def validate_orderedProducts(self, value):
		new_value = []

		for odp in value:
			productId = odp["productId"]
			quantity = odp["quantity"]

			if not Product.objects.filter(id=productId).exists():
				raise serializers.ValidationError(f"Le produit dont l'identifiant {productId} n'existe pas.")

			new_value.append((
				Product.objects.get(id=productId), 
				quantity
			))

		return new_value

class OrderCreateSerializer(OrderWriteSerializer):
	def create(self, validated_data):
		orderedProducts = validated_data.pop("orderedProducts")

		order = Order.objects.create(**validated_data)

		# add ordered products
		# data
		for product, quantity in orderedProducts:
			order.add_product(product, quantity)

		order.save()

		return order

class OrderUpdateSerializer(OrderWriteSerializer):
	orderedProducts = serializers.ListField(write_only=True, required=False)
