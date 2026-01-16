from rest_framework import serializers
from .models import Category, Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'name']


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id', )

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('id', 'created_at')

class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    category_details = serializers.SerializerMethodField()
    class Meta:
        model = Product
        # exclude = ()
        fields = [
            'id',
            'name',
            'description',
            'price',
            'created_at',
            'category_details',  # Custom
            'images'  # Nested
        ]

    def get_category_details(self, obj):
        if obj.category:
            return {
                "id": obj.category.id,
                "title": obj.category.title,
                "slug": obj.category.slug
            }
        return "NO category"



class ParentCategoryModelSerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    # products = ProductListSerializer(many=True, read_only=True)
    # product_count = serializers.SerializerMethodField()

    # def get_product_count(self,obj):
    #     count = obj.products.all().count()
    #     for child in obj.children.filter(is_active=True):
    #         count+=child.product_count
    #
    #     return count

    class Meta:
        model = Category
        # exclude = ()
        fields = ('id', 'title', 'slug', 'image', 'product_count')



