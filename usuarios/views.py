from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
from .models import Perfil

# Create your views here.


class UsuarioCreate(CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        url = super().form_valid(form)
        self.object.save()
        Perfil.objects.create(usuario=self.object)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de Novo Usuário'
        return context
