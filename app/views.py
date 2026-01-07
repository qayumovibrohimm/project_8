from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car
from .serializer import CarModelSerializer
from rest_framework import status
from datetime import datetime

# Create your views here.

class CarListApiView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializers = CarModelSerializer(cars,many=True)
        return Response(serializers.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = CarModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'data':'Car successfully created.',
                    'create':True,
                    'created_at':str(datetime.now())
                },
                status = status.HTTP_201_CREATED
            )
        return Response({'data':'something is wrong'})


class CarDetailApiView(APIView):
    def get(self, request):
        car = Car.objects.all().first()
        if not car:
            return Response({'data': 'Car not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarModelSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self,request):
        car = Car.objects.all().first()
        if not car:
            return Response({'data': 'Car not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarModelSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'data': 'Car successfully updated.',
                    'update': True,
                    'updated_at': str(datetime.now())
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        car = Car.objects.all().first()
        if not car:
            return Response({'data': 'Car not found.'}, status=status.HTTP_404_NOT_FOUND)

        car.delete()
        return Response(
        {
                'data': 'Car successfully deleted.',
                'deleted': True,
                'deleted_at': str(datetime.now())
            },
            status=status.HTTP_204_NO_CONTENT
        )

# class CarListApiView(APIView):
#     def get(self, request):
#             cars = [
#                         {
#                             "name":"Gentra",
#                             "color":"Black",
#                             "price":8999.00
#                         },
#                         {
#                             "name":"Matiz",
#                             "color":"Black",
#                             "price":8999.00
#                         },
#                         {
#                             "name":"Spark",
#                             "color":"Black",
#                             "price":8999.00
#                         }
#                 ]
#             return Response(cars)