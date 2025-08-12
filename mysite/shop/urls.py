from django.contrib import admin
from django.urls import path
from shop.views import about


urlpatterns = [
    path('', about, name='about'),
]
