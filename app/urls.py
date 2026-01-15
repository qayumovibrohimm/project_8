from django.urls import path, include
from .views import ParentCategoryListApiView, ChildrenCategoryByCategorySlug, CategoryCreateApiView, CategoryDetailApiView

urlpatterns = [
    path("", ParentCategoryListApiView.as_view()),
    path("category/<slug:slug>/", ChildrenCategoryByCategorySlug.as_view()),
    path("category/create", CategoryCreateApiView.as_view()),
    path('category/<slug:slug>/rud', CategoryDetailApiView.as_view()),
]