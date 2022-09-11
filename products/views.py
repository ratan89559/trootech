from rest_framework import viewsets
from rest_framework.response import Response

from products.models import Category, Product
from products.serializers import ProductSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow user to perform CRUD operations in the category
    """
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer

    def get_queryset(self):
        # Will show all the sub categories in under parent categories
        if self.action == 'list':
            return Category.objects.filter(parent__isnull=True)
        else:
            return Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow user to perform CRUD operations in the product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
