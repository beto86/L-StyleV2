from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class UsuarioCreate(CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Aluno")
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de Novo Usuário'
        return context


class PerfilUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Perfil
    fields = ['nome_completo', 'ra', 'cpf', 'telefone',
              'sexo', 'data_nascimento', 'endereco', 'numero',
              'cep', 'cidade', 'estado', 'pais']
    success_url = reverse_lazy("index")

    # def form_valid(self, form):
    #grupo_id = self.request.POST.get("grupo")
    #usuario = User.objects.get(pk=self.request.user.id)
    #self.object = form.save()
    # usuario.groups.add(grupo_id)
    # self.object.groups.add(grupo)
    # self.object.save()
    # return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Meus dados pessoais'
        return context


class AlterarSenha(PasswordChangeView):
    from_class = PasswordChangeForm
    template_name = 'cadastros/form.html'
    model = User
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Alterar Senha'
        return context


class AlunoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Perfil
    template_name = 'listas/alunos.html'

    def get_queryset(self):
        self.object_list = Perfil.objects.filter(
            usuario__groups__id=3)
        return self.object_list
