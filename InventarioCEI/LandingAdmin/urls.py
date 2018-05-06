from django.urls import path
from . import views

app_name = 'LandingAdmin'

urlpatterns = [
    # /landingAdmin/
    path('', views.index, name='index'),

]