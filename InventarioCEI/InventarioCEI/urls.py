from django.urls import include, path

from userSystem.views import userSystem, usuarios, administrador

urlpatterns = [
    path('', include('userSystem.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', userSystem.SignUpView.as_view(), name='signup'),
    path('accounts/signup/usuarios/', usuarios.UsuariosSignUpView.as_view(), name='usuarios_signup'),
    path('accounts/signup/administrador54r3464643w3frrhey54etfegrtjh46e4t53rf44g53nh5gwfedfgfh4634fefvdhfth45634rwg/', administrador.AdministradorSignUpView.as_view(), name='administrador_signup'),
]
