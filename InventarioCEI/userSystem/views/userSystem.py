from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup_form.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_administrador:
            return redirect('administrador:admin_landing_view')
        else:
            return redirect('usuarios:user_landing_view')
    return render(request, 'userSystem/home.html')