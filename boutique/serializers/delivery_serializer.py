from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
import phonenumbers
from boutique.models import Delivery, Order
from .order_serializer import OrderDetailSerializer


class DeliverySerializer(ModelSerializer):
	class Meta:
		model = Delivery
		fields = ("id", "order", "status", "address", "phoneNumber", "lat", "lon", "date_created", "date_updated")


class DeliveryListSerializer(DeliverySerializer):
	pass

class DeliveryDetailSerializer(DeliverySerializer):
	order = SerializerMethodField()

	def get_order(self, instance):
		queryset = instance.order

		serializer = OrderDetailSerializer(queryset, many=True)

		return serializer.data

class DeliveryWriteSerializer(DeliverySerializer):
	
	class Meta(DeliverySerializer.Meta):
		extra_kwargs = {
			"id" :{"read_only": True},
			"date_created": {"read_only": True},
			"date_updated": {"read_only": True},
			"status": {"read_only": True},
		}
	
	def validate_phoneNumber(self, value):
		try:
			parsed_number = phonenumbers.parse(value, None)
			
			if not phonenumbers.is_valid_number(parsed_number):
				raise serializers.ValidationError("Le numéro de téléphone n'est pas valide.")
		
		except phonenumbers.phonenumberutil.NumberParseException:
			raise serializers.ValidationError("Le numéro de téléphone n'est pas valide.")
		
		return value

class DeliveryCreateSerializer(DeliveryWriteSerializer):
	pass

class DeliveryUpdateSerializer(DeliveryWriteSerializer):
	pass