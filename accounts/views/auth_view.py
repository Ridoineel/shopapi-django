from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from accounts.serializers import UserSignupSerializer
from boutique.views.base import BaseViewSet

User = get_user_model()

class AuthViewSet(BaseViewSet, ModelViewSet):
	# http_method_names = ['get', 'put', 'patch', 'delete']
	serializer_class = UserSignupSerializer
	create_serializer_class = UserSignupSerializer
	
	def get_queryset(self):
		queryset = User.objects.all()

		return queryset

	@action(detail=False, methods=["POST"])
	def signup(self, request):
		return self.create(request)
	
	# @action(detail=False, methods=["POST"])
	# def signin(self, request):
	# 	return self.create(request)
	
	