from django.urls import path

from . import views

urlpatterns = [
    path('', views.busqueda_simple, name='simple'),
    path('avanzada/', views.busqueda_avanzada, name='avanzada')
]
