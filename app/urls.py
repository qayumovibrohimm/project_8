from django.urls import path, include
from .views import CarListApiView

urlpatterns = [
    path("cars/", CarListApiView.as_view()),
]