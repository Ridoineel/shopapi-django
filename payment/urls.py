from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.SimpleRouter()

# router.register("category", CategoryViewSet, basename="categorie")

urlpatterns = [
    path("", include(router.urls)),
]