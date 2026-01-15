from rest_framework import serializers
from .models import Category


class ParentCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id', )

