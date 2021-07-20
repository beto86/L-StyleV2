from django.shortcuts import render
from .models import Questionario, Questao, Teste, Tentativa, Opcao, Resposta
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from braces.views import GroupRequiredMixin
from .forms import TesteILSKolbForm


# Create your views here.


class QuestionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questionario
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questionarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Questionario'
        return context


class QuestaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questao
    fields = ['questionario', 'descricao', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Questão'
        return context


class OpcaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Opcao
    fields = ['questao', 'descricao', 'imagem',
              'video', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-opcoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Opção'
        return context


class TentativaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Tentativa
    fields = ['teste', 'aluno', 'concluiu']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tentativas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Tentativa'
        return context


class TesteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Teste
    fields = ['descricao', 'professor',
              'questionario', 'turma', 'chave_acesso', 'ativo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-testes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Teste'
        return context


################ UPDATE ####################


class QuestionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questionario
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questionarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Questionario'
        return context


class QuestaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questao
    fields = ['questionario', 'descricao', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Questão'
        return context


class OpcaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Opcao
    fields = ['questao', 'descricao', 'imagem',
              'video', 'ordem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-opcoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Turma'
        return context


class TesteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Teste
    fields = ['descricao', 'professor',
              'questionario', 'turma', 'chave_acesso', 'ativo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-testes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Teste'
        return context


################ DELETE ####################


class QuestionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-questionarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Questionário'
        context['titulo2'] = 'o questionário'
        return context


class QuestaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-questoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir questão'
        context['titulo2'] = 'a questão'
        return context


class OpcaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Opcao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-opcoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Opcão'
        context['titulo2'] = 'a opcão'
        return context


class TesteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Teste
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-testes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Teste'
        context['titulo2'] = 'a teste'
        return context

################ LIST ####################


class QuestionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questionario
    template_name = 'cadastros/listas/questionario.html'


class QuestaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Questao
    template_name = 'cadastros/listas/questao.html'


class OpcaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Opcao
    template_name = 'cadastros/listas/opcao.html'


class TentativaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Tentativa
    template_name = 'cadastros/listas/tentativa.html'


class TesteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Teste
    template_name = 'cadastros/listas/teste.html'


class RespostaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Resposta
    template_name = 'cadastros/listas/resposta.html'

############# OUTRAS PAGINAS DO TESTE ##############


class TesteILSKolbView(FormView):
    template_name = "teste-ils-kolb.html"
    form_class = TesteILSKolbForm
    success_url = reverse_lazy("resposta")

    def form_valid(self, form):

        # Verificar se todos os dados foram preenchidos
        questionario = Questionario.objects.get(pk=1)

        # Contar questões de Kolb
        num_q = Questao.objects.filter(
            questionario__pk=1).count()  # Sempre O Kolb com id 1

        # Cria uma lista numérica com a ordem das questões
        questoes = range(1, num_q+1)
        # Cria uma lista numérica de opções
        opcoes = range(1, 5)

        # Validar respostas
        respostas = True

        # Para cada número das questões
        for q in questoes:
            # Para cada opção que a gente tem de cada questão
            for opc in opcoes:
                # Gera o name igual lá no template
                name = f"opc_{q}_{opc}"
                # pega o valor desse input que ficou selecionado no template
                valor = self.request.POST.get(name)
                # Se input não foi preenchido ou se for algum outro valor
                if(valor is None or valor not in ["1", "2", "3", "4"]):
                    # Adiciona uma mensagem de erro no formulário
                    form.add_error(
                        None, f"Você não respondeu corretamente a opção {opc} da questão {q}.")
                    # Muda para falso para não submeter com sucesso o formulário
                    respostas = False

        # Se não preencheu tudo, retorna ao formulário com as mensagens de erro encontradas
        # if(respostas == False):
        #    return self.form_invalid(form)
        # else:
            # Caso esteja tudo certo...

            # Criar uma Tentativa
        teste = Teste.objects.get(pk=self.kwargs['pk_teste'])
        tentativa = Tentativa.objects.create(
            teste=teste, aluno=self.request.user)

        # para cada tentativa, criar uma Resposta
        # Para cada número das questões
        for q in questoes:
            questao = Questao.objects.get(questionario=questionario, ordem=q)
            # Para cada opção que a gente tem de cada questão
            for opc in opcoes:
                # Gera o name igual lá no template
                name = f"opc_{q}_{opc}"
                opcao = Opcao.objects.get(questao=questao, ordem=opc)

                # pega o valor desse input que ficou selecionado no template
                valor = self.request.POST.get(name)
                # Criar um objeto Resposta para cada um com a tentativa, teste, opção, etc

                resp = Resposta.objects.create(
                    tentativa=tentativa, opcao=opcao, valor=valor, aluno=self.request.user)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionario'] = Questionario.objects.get(pk=1)

        context['questoes'] = Questao.objects.filter(
            questionario=context['questionario'])

        context['opcoes'] = {}

        for q in context['questoes']:
            context['opcoes'][q.pk] = Opcao.objects.filter(questao=q)

        return context


class RespostaView(DetailView):
    template_name = 'resposta.html'
    model = Teste

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionario'] = Questionario.objects.get(pk=1)
        context['tentativas'] = Tentativa.objects.filter(teste=self.object)

        #context['respostas'] = {}
        # for t in context['tentativas']:
        #    context['respostas'][t.pk] = Resposta.objects.filter(tentativa=t)

        return context
