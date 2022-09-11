from django.contrib import admin

from products.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin panel manage list view and add search feature in admin panel
    """
    list_display = ('name', 'description', 'sub_categories')
    search_fields = ('name', 'description')

    @staticmethod
    def sub_categories(obj):
        return list(obj.sub_categories.all().values_list("name", flat=True))


class ProductAdmin(admin.ModelAdmin):
    """
    Product admin panel manage list view and add search feature in admin panel
    """
    list_display = ('name', 'price', 'get_categories')
    search_fields = ('name', 'price')

    @staticmethod
    def get_categories(obj):
        return list(obj.categories.all().values_list("name", flat=True))


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
