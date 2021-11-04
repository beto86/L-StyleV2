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
from django.forms import ModelForm
from cadastros.models import Turma
from KolbStyleTeste.models import Tentativa


# Create your views here.


class ProfessorForm(ModelForm):
    template_name = 'cadastros/form.html'

    class Meta():
        model = Perfil
        fields = ['nome_completo', 'cpf', 'telefone',
                  'sexo', 'data_nascimento', 'endereco', 'numero',
                  'cep', 'cidade', 'estado', 'pais']


class AlunoForm(ModelForm):
    template_name = 'cadastros/form.html'

    class Meta():
        model = Perfil
        fields = ['nome_completo', 'ra', 'cpf', 'telefone',
                  'sexo', 'data_nascimento', 'endereco', 'numero',
                  'cep', 'cidade', 'estado', 'pais']


class PerfilUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Perfil
    success_url = reverse_lazy("index")

    def get_form_class(self):
        if self.request.user.groups.filter(name='Professor').exists():
            return ProfessorForm
        return AlunoForm

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

        queryset = Tentativa.objects.filter(
            teste__professor=self.request.user).select_related('usuario')  # .distinct('usuario')
        self.object_list = []
        for t in queryset:
            self.object_list.append(t.usuario.perfil)

        return self.object_list


class ProfessorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Perfil
    template_name = 'listas/professor.html'

    def get_queryset(self):
        self.object_list = Perfil.objects.filter(
            usuario__groups__id=2)
        return self.object_list


class AlunoCreate(CreateView):
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
        context['titulo'] = 'Registro de Novo Aluno'
        return context


class ProfessorCreate(CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Professor")
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de Novo Professor'
        return context
