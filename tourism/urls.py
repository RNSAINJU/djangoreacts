
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('hotels.urls')),
    path('', include('frontend.urls')),
]
