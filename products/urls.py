from django.urls import path, include
from rest_framework import routers

from products.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
