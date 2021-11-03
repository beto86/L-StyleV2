from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Instituicao, Turma, Curso
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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Instituição'
        return context


class TurmaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Turma
    fields = ['nome', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turmas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['curso'].queryset = Curso.objects.filter(
            usuario=self.request.user)
        context['form'].fields['instituicao'].queryset = Instituicao.objects.filter(
            usuario=self.request.user)
        context['titulo'] = 'Cadastro de Turma'
        return context


class CursoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Curso
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cursos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Curso'
        return context

################ UPDATE ####################


class InstituicaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Instituicao
    fields = ['nome', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-instituicoes')

    def get_object(self):
        self.object = get_object_or_404(
            Instituicao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Instituição'
        return context


class TurmaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Turma
    fields = ['nome', 'periodo',
              'ano', 'curso', 'turno', 'instituicao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turmas')

    def get_object(self):
        self.object = get_object_or_404(
            Turma, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['curso'].queryset = Curso.objects.filter(
            usuario=self.request.user)
        context['form'].fields['instituicao'].queryset = Instituicao.objects.filter(
            usuario=self.request.user)
        context['titulo'] = 'Editar Cadastro de Turma'
        return context


class CursoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Curso
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cursos')

    def get_object(self):
        self.object = get_object_or_404(
            Curso, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Curso'
        return context


################ DELETE ####################


class InstituicaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Instituicao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-instituicoes')

    def get_object(self):
        self.object = get_object_or_404(
            Instituicao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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

    def get_object(self):
        self.object = get_object_or_404(
            Turma, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Turma'
        context['titulo2'] = 'a turma'
        return context


class CursoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cursos')

    def get_object(self):
        self.object = get_object_or_404(
            Curso, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Curso'
        context['titulo2'] = 'o curso'
        return context


################ LIST ####################


class InstituicaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Instituicao
    template_name = 'cadastros/listas/instituicao.html'

    def get_queryset(self):
        self.object_list = Instituicao.objects.filter(
            usuario=self.request.user)
        return self.object_list


class TurmaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Turma
    template_name = 'cadastros/listas/turma.html'

    def get_queryset(self):
        self.object_list = Turma.objects.filter(usuario=self.request.user)
        return self.object_list


class CursoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Curso
    template_name = 'cadastros/listas/curso.html'

    def get_queryset(self):
        self.object_list = Curso.objects.filter(usuario=self.request.user)
        return self.object_list
