from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Endereco, Instituicao, Turma
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class EnderecoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['cep', 'rua', 'numero',
              'complemento', 'bairro', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-enderecos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Endereços'
        return context


class InstituicaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-instituicoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Instituição'
        return context


class TurmaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
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


class EnderecoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['cep', 'rua', 'numero',
              'complemento', 'bairro', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-enderecos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Endereço'
        return context


class InstituicaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
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


class EnderecoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-enderecos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Endereço'
        context['titulo2'] = 'o endereço'
        return context


class InstituicaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Instituicao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-instituicoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir instituição'
        context['titulo2'] = 'a instituição'
        return context


class TurmaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Turma
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-turmas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Turma'
        context['titulo2'] = 'a turma'
        return context


################ LIST ####################


class EnderecoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Endereco
    template_name = 'cadastros/listas/endereco.html'


class InstituicaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Instituicao
    template_name = 'cadastros/listas/instituicao.html'


class TurmaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Turma
    template_name = 'cadastros/listas/turma.html'
