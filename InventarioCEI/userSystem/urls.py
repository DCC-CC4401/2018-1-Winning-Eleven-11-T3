from django.urls import include, path

from .views import userSystem, usuarios, administrador

urlpatterns = [

    path('usuarios/', include(([
        path('', usuarios.LandingUserView.as_view(), name='user_landing_view'),
    ], 'userSystem'), namespace='usuarios')),

    path('administrador/', include(([
        path('', administrador.LandingAdminView.as_view(), name='admin_landing_view'),
    ], 'userSystem'), namespace='administrador')),
]