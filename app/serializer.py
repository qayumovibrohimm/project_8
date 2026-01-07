from rest_framework import serializers
from .models import Car

# class CarSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     color = serializers.CharField()
#     price = serializers.DecimalField(max_digits=14, decimal_places=2)



class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ()