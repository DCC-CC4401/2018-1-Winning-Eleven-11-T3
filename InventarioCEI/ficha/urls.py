from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('<int:anId>/', views.viewitem, name='viewitem'),
    path('ajax/guardar_titulo/', views.guardar_titulo, name='guardar_titulo'),
    path('ajax/guardar_descripcion/', views.guardar_descripcion, name='guardar_descripcion'),
    path('ajax/cambiar_estado/', views.cambiar_estado, name='cambiar_estado'),
    path('ajax/cambiar_imagen/', views.cambiar_imagen, name='cambiar_imagen'),

]
