from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    # /inventario/
    path('', views.index, name='index'),

]