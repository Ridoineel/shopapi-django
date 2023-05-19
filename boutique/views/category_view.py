from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

from boutique.models import Category
from boutique.serializers import CategoryListSerializer, CategoryDetailSerializer, CategoryUpdateSerializer
from boutique.views.base import BaseViewSet
from boutique.permissions import IsAdminAuthenticated

class CategoryViewSet(BaseViewSet, ReadOnlyModelViewSet):
	serializer_class = CategoryListSerializer
	detail_serializer_class = CategoryDetailSerializer

	def get_queryset(self):
		return Category.objects.filter(active=True)

class AdminCategoryViewSet(BaseViewSet, ModelViewSet):
	serializer_class = CategoryListSerializer
	detail_serializer_class = CategoryDetailSerializer
	update_serializer_class = CategoryUpdateSerializer
	permission_classes =  [IsAdminAuthenticated]

	def get_queryset(self):
		return Category.objects.all()