from django.urls import path

from . import views

urlpatterns = [
    path('<int:anId>/', views.viewitem, name='viewitem'),
]
