from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from boutique.views import \
    CategoryViewSet, \
    ProductViewSet, \
    AdminCategoryViewSet, \
    AdminProductViewSet, \
    OrderViewSet, \
    DeliveryViewSet

from accounts.views import AuthViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Boutique API",
      default_version='v1',
      description="description",
      terms_of_service="https://www.google.com/policies/terms/",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.SimpleRouter()

router.register("category", CategoryViewSet, basename="categorie")
router.register("product", ProductViewSet, basename="product")
router.register("order", OrderViewSet, basename="order")
router.register("admin/category", AdminCategoryViewSet, basename="admin-categorie")
router.register("admin/product", AdminProductViewSet, basename="admin-product")
router.register("auth", AuthViewSet, basename="auth")
router.register("delivery", DeliveryViewSet, basename="delivery")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include(router.urls)),
    path("api/payment/", include("payment.urls")),
    ##
    path("api/auth/signin", TokenObtainPairView.as_view(), name="auth-token"),
    path("api/auth/token-refresh", TokenRefreshView.as_view(), name="refresh-token"),
    ###
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]
