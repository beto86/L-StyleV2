from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Endereco, Instituicao, Turma
from django.urls import reverse_lazy

# Create your views here.


class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['cep', 'rua', 'numero',
              'complemento', 'bairro', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class InstituicaoCreate(CreateView):
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class TurmaCreate(CreateView):
    model = Turma
    fields = ['nome', 'ra', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


################ UPDATE ####################

class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = ['cep', 'rua', 'numero',
              'complemento', 'bairro', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class InstituicaoUpdate(UpdateView):
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class TurmaUpdate(UpdateView):
    model = Turma
    fields = ['nome', 'ra', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


################ DELETE ####################


class EnderecoDelete(DeleteView):
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')


class InstituicaoDelete(DeleteView):
    model = Instituicao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')


class TurmaDelete(DeleteView):
    model = Turma
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
