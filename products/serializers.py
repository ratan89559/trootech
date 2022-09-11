from rest_framework import serializers

from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField("get_subcategories", read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'sub_categories', 'parent']
        extra_kwargs = {
            "parent": {"write_only": True}
        }

    @staticmethod
    def get_subcategories(obj):
        return CategorySerializer(obj.sub_categories, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
