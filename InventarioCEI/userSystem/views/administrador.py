from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import administrador_required
from ..forms import  AdministradorSignUpForm
from ..models import User, Usuarios


class AdministradorSignUpView(CreateView):
    model = User
    form_class = AdministradorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'administrador'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('administrador:admin_landing_view')



@method_decorator([login_required, administrador_required], name='dispatch')
class LandingAdminView(ListView):
    model = User
    ordering = ('name',)
    context_object_name = 'admin_landing'
    template_name = 'userSystem/administrador/admin_landing_view.html'