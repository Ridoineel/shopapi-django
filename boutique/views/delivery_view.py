from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from boutique.models import Delivery
from boutique.serializers import  DeliverySerializer, DeliveryCreateSerializer, DeliveryDetailSerializer, DeliveryListSerializer, DeliveryUpdateSerializer
from boutique.views.base import BaseViewSet

class DeliveryViewSet(BaseViewSet, ModelViewSet):
	serializer_class = DeliverySerializer
	detail_serializer_class = DeliveryDetailSerializer
	create_serializer_class = DeliveryCreateSerializer
	update_serializer_class  = DeliveryUpdateSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		user: User = self.request.user

		if user.is_superuser or user.is_staff:
			queryset = Delivery.objects.all()
		else: # user is a simple user
			queryset = Delivery.objects.filter(order__user=user)
		
		return queryset
	
	def perform_create(self, serializer: DeliveryCreateSerializer):
		user: User = self.request.user
		order = serializer.validated_data.get("order")

		if order.client != user:
			raise PermissionDenied("Vous n'avez aucune permission sur cette commande.")

		serializer.save()