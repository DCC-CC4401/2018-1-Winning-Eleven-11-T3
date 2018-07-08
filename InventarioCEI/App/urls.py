from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articulos/', views.busqueda_simple, name='simple'),
    path('articulos/avanzada/', views.busqueda_avanzada, name='avanzada'),
    path('articulos/<int:anId>/', views.viewitem, name='viewitem'),
    path('articulos/ajax/guardar_titulo/', views.guardar_titulo, name='guardar_titulo'),
    path('articulos/ajax/guardar_descripcion/', views.guardar_descripcion, name='guardar_descripcion'),
    path('articulos/ajax/cambiar_estado/', views.cambiar_estado, name='cambiar_estado'),
    path('articulos/ajax/cambiar_imagen/', views.cambiar_imagen, name='cambiar_imagen'),
    path('articulos/ajax/enviar_solicitud/', views.enviar_solicitud, name='enviar_solicitud'),
    path('espacios/', views.espacios, name='espacios'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
]
