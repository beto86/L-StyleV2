from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Instituicao, Turma
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# Create your views here.


class InstituicaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-instituicoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Instituição'
        return context


class TurmaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Turma
    fields = ['nome', 'ra', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turmas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Turma'
        return context

################ UPDATE ####################


class InstituicaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-instituicoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Instituição'
        return context


class TurmaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Turma
    fields = ['nome', 'ra', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turmas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Turma'
        return context


################ DELETE ####################


class InstituicaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Instituicao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-instituicoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir instituição'
        context['titulo2'] = 'a instituição'
        return context


class TurmaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Turma
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-turmas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Turma'
        context['titulo2'] = 'a turma'
        return context


################ LIST ####################


class InstituicaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Instituicao
    template_name = 'cadastros/listas/instituicao.html'


class TurmaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Turma
    template_name = 'cadastros/listas/turma.html'
