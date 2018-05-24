from django.urls import path

from . import views

urlpatterns = [
    path('', views.busqueda_simple, name='simple'),
    path('avanzada/', views.busqueda_avanzada, name='avanzada'),
    path('<int:anId>/', views.viewitem, name='viewitem'),
    path('ajax/guardar_titulo/', views.guardar_titulo, name='guardar_titulo'),
    path('ajax/guardar_descripcion/', views.guardar_descripcion, name='guardar_descripcion'),
    path('ajax/cambiar_estado/', views.cambiar_estado, name='cambiar_estado'),
    path('ajax/cambiar_imagen/', views.cambiar_imagen, name='cambiar_imagen'),
    path('ajax/enviar_solicitud/', views.enviar_solicitud, name='enviar_solicitud'),
]
