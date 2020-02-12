from django.urls import path, include
from . import views

urlpatterns = [
    path('api/hotel/', views.HotelListCreate.as_view() ),
]