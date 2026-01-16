from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.ParentCategoryListApiView.as_view()),
    path("category/<slug:slug>/", views.ChildrenCategoryByCategorySlug.as_view()),
    path("category/<slug:slug>/products/", views.ProductListByChildCategorySlug.as_view()),
    path("category/create", views.CategoryCreateApiView.as_view()),
    path('category/<slug:slug>/rud', views.CategoryDetailApiView.as_view()),
    path("create/product", views.ProductCreateApiView.as_view()),
    path("products", views.ProductListApiView.as_view()),

]