from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from unicodedata import category
from .models import Category, Product
from rest_framework import status, permissions
from datetime import datetime
from .serializer import (ParentCategoryModelSerializer,
                         CreateCategorySerializer,
                         CreateProductSerializer,
                         ProductListSerializer)
from .permissions import IsKayumBlocked, WorkDay, CanUpdateWithin4Hours

# Create your views here.
class ParentCategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ParentCategoryModelSerializer

    def get_queryset(self):
        queryset = Category.objects.filter(parent__isnull = True)
        return queryset

class ChildrenCategoryByCategorySlug(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ParentCategoryModelSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        queryset = Category.objects.filter(slug = category_slug).first()
        if not queryset:
            return Category.objects.none()
        return queryset.children.all()

class  ProductListByChildCategorySlug(ListAPIView):
    serializer_class = ProductListSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [WorkDay]

    def get_queryset(self):
        parent_slug = self.kwargs['slug']
        child_slug = self.kwargs['child_slug']
        parent_category = Category.objects.get(slug=parent_slug)
        child_category = parent_category.children.filter(slug=child_slug).first()
        if not child_category:
            return Category.objects.none()

        return child_category.products.all()

class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer

class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]



class ProductCreateApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [CanUpdateWithin4Hours]



























# class CarListApiView(APIView):
#     def get(self, request):
#         cars = Car.objects.all()
#         serializers = CarModelSerializer(cars,many=True)
#         return Response(serializers.data, status = status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CarModelSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'data':'Car successfully created.',
#                     'create':True,
#                     'created_at':str(datetime.now())
#                 },
#                 status = status.HTTP_201_CREATED
#             )
#         return Response({'data':'something is wrong'})
#
#
# class CarDetailApiView(APIView):
#     def get(self, request):
#         car = Car.objects.all().first()
#         if not car:
#             return Response({'data': 'Car not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = CarModelSerializer(car)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def put(self,request):
#         car = Car.objects.all().first()
#         if not car:
#             return Response({'data': 'Car not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = CarModelSerializer(car, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'data': 'Car successfully updated.',
#                     'update': True,
#                     'updated_at': str(datetime.now())
#                 },
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request):
#         car = Car.objects.all().first()
#         if not car:
#             return Response({'data': 'Car not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#         car.delete()
#         return Response(
#         {
#                 'data': 'Car successfully deleted.',
#                 'deleted': True,
#                 'deleted_at': str(datetime.now())
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )
#
# # class CarListApiView(APIView):
# #     def get(self, request):
# #             cars = [
# #                         {
# #                             "name":"Gentra",
# #                             "color":"Black",
# #                             "price":8999.00
# #                         },
# #                         {
# #                             "name":"Matiz",
# #                             "color":"Black",
# #                             "price":8999.00
# #                         },
# #                         {
# #                             "name":"Spark",
# #                             "color":"Black",
# #                             "price":8999.00
# #                         }
# #                 ]
# #             return Response(cars)