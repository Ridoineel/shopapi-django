from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

from boutique.models import Order
from boutique.serializers import OrderDetailSerializer, OrderListSerializer, OrderCreateSerializer, OrderUpdateSerializer
from boutique.views.base import BaseViewSet
from django.contrib.auth.models import User
# from boutique.permissions import IsAdminAuthenticated

class OrderViewSet(BaseViewSet, ModelViewSet):
	serializer_class = OrderListSerializer
	create_serializer_class = OrderCreateSerializer
	detail_serializer_class = OrderDetailSerializer
	update_serializer_class = OrderUpdateSerializer
	permission_classes =  [IsAuthenticated]

	def get_queryset(self):
		user: User = self.request.user

		if user.is_superuser or user.is_staff:
			queryset = Order.objects.all()
		else: # user is a simple user
			queryset = Order.objects.filter(client=user)
		
		return queryset
	
	def perform_create(self, serializer):
		user = self.request.user

		serializer.save(client=user)
	
	# @action(permission_classes=[VotrePermissionClasse])

	# def get_permission_classes(self):
	# 	PERMISSION_CLASSES = {
	# 		# "create": ,
	# 		# "list": ,
	# 		# "retrieve": ,
	# 		# "update": ,
	# 		# "partial_update": ,
	# 	}

	# 	permission_classes = PERMISSION_CLASSES.get(self.action)
		
	# 	if permission_classes is not None:
	# 		return permission_classes

	# 	return super().get_permission_classes()