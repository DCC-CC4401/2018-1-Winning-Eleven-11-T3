from django.urls import path

from . import views

urlpatterns = [
    path('', views.articulos, name='articulos'),
]