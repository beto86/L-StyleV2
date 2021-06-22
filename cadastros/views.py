from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Endereco, Instituicao, Turma
from django.urls import reverse_lazy

# Create your views here.


class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['cep', 'rua', 'numero',
              'complemento', 'bairro', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-enderecos')


class InstituicaoCreate(CreateView):
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-instituicoes')


class TurmaCreate(CreateView):
    model = Turma
    fields = ['nome', 'ra', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turmas')


################ UPDATE ####################

class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = ['cep', 'rua', 'numero',
              'complemento', 'bairro', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-enderecos')


class InstituicaoUpdate(UpdateView):
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-instituicoes')


class TurmaUpdate(UpdateView):
    model = Turma
    fields = ['nome', 'ra', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turmas')


################ DELETE ####################


class EnderecoDelete(DeleteView):
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-enderecos')


class InstituicaoDelete(DeleteView):
    model = Instituicao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-instituicoes')


class TurmaDelete(DeleteView):
    model = Turma
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-turmas')


################ LIST ####################


class EnderecoList(ListView):
    model = Endereco
    template_name = 'cadastros/listas/endereco.html'


class InstituicaoList(ListView):
    model = Instituicao
    template_name = 'cadastros/listas/instituicao.html'


class TurmaList(ListView):
    model = Turma
    template_name = 'cadastros/listas/turma.html'
