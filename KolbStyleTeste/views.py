from django.shortcuts import render
from .models import Questionario, Questao, Teste, Tentativa, Opcao, Resposta
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class QuestionarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Questionario
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questionario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Questionario'
        return context


class QuestaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Questao
    fields = ['questionario', 'descricao', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questionario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Questão'
        return context


class OpcaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Opcao
    fields = ['questao', 'descricao', 'imagem',
              'video', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ordem')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Opção'
        return context


class TentativaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tentativa
    fields = ['teste', 'aluno', 'data',
              'concluiu']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tentativa')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Tentativa'
        return context


class TesteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Teste
    fields = ['descricao', 'professor',
              'questionario', 'turma', 'chave_acesso', 'ativo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-teste')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Teste'
        return context


################ UPDATE ####################


class QuestionarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Questionario
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questionario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Questionario'
        return context


class QuestaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Questao
    fields = ['questao', 'descricao', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Questão'
        return context


class OpcaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Opcao
    fields = ['questao', 'descricao', 'imagem',
              'video', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-opcao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Turma'
        return context


class TesteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Opcao
    fields = ['descricao', 'professor',
              'questionario', 'turma', 'turma', 'chave_acesso', 'ativo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-testes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Teste'
        return context


################ DELETE ####################


class QuestionarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Questionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-questionarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Questionário'
        context['titulo2'] = 'o questionário'
        return context


class QuestaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Questao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-questao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir questão'
        context['titulo2'] = 'a questão'
        return context


class OpcaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Opcao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-opcao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Opcão'
        context['titulo2'] = 'a opcão'
        return context


class TesteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Teste
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-teste')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Teste'
        context['titulo2'] = 'a teste'
        return context

################ LIST ####################


class QuestionarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Questionario
    template_name = 'cadastros/listas/questionario.html'


class QuestaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Questao
    template_name = 'cadastros/listas/questao.html'


class OpcaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Opcao
    template_name = 'cadastros/listas/opcao.html'


class TentativaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tentativa
    template_name = 'cadastros/listas/tentativa.html'


class TesteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Teste
    template_name = 'cadastros/listas/teste.html'


class RespostaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Resposta
    template_name = 'cadastros/listas/resposta.html'
