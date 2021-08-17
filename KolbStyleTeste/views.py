from django.shortcuts import render, get_object_or_404
from .models import Questionario, Questao, Teste, Tentativa, Opcao, Resposta, Estilo, FormaAprendizagem
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from braces.views import GroupRequiredMixin
from .forms import TesteILSKolbForm
from django.contrib.auth.models import User

from django.db.models import Sum

from django.views.generic import TemplateView

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
              'video', 'ordem', 'forma_aprendizagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-opcoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Opção'
        return context


class TentativaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor", u"Aluno"]
    model = Tentativa
    fields = ['teste', 'aluno', 'concluiu']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tentativas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Tentativa'
        return context


class TesteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Teste
    fields = ['descricao', 'questionario', 'turma', 'chave_acesso', 'ativo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-testes')

    def form_valid(self, form):
        form.instance.professor = self.request.user
        url = super().form_valid(form)
        return url

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
              'video', 'ordem', 'forma_aprendizagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-opcoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cadastro de Opção'
        return context


class TesteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Teste
    fields = ['descricao', 'questionario', 'turma', 'chave_acesso', 'ativo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-testes')

    def get_object(self):
        self.object = get_object_or_404(
            Teste, pk=self.kwargs['pk'], professor=self.request.user)
        return self.object

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
    group_required = [u"Administrador", u"Professor"]
    model = Teste
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-testes')

    def get_object(self):
        self.object = get_object_or_404(
            Teste, pk=self.kwargs['pk'], professor=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Teste'
        context['titulo2'] = 'a teste'
        return context

################ LIST ####################


class QuestionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Questionario
    template_name = 'cadastros/listas/questionario.html'


class QuestaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Questao
    template_name = 'cadastros/listas/questao.html'


class OpcaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Opcao
    template_name = 'cadastros/listas/opcao.html'


class TentativaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor", u"Aluno"]
    model = Tentativa
    template_name = 'cadastros/listas/tentativa.html'

    def get_queryset(self):
        self.object_list = Tentativa.objects.filter(usuario=self.request.user)
        return self.object_list


class TesteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Teste
    template_name = 'cadastros/listas/teste.html'

    def get_queryset(self):
        self.object_list = Teste.objects.filter(professor=self.request.user)
        return self.object_list


class RespostaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Professor"]
    model = Resposta
    template_name = 'cadastros/listas/resposta.html'

    def get_queryset(self):
        self.object_list = Resposta.objects.filter(tentativa__usuario=self.request.user)
        return self.object_list

############# OUTRAS PAGINAS DO TESTE ##############


class IniciarTesteView(TemplateView):
    template_name = 'iniciar-teste.html'


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
        #     return self.form_invalid(form)
        # else:
            # Caso esteja tudo certo...

            # Criar uma Tentativa
        teste = get_object_or_404(Teste, pk=self.kwargs['pk_teste'], chave_acesso=self.kwargs['chave'], ativo=True)
        tentativa = Tentativa.objects.create(
            teste=teste, usuario=self.request.user)

        # para cada tentativa, criar uma Resposta
        # Para cada número das questões
        for q in questoes:
            questao = Questao.objects.get(
                questionario=questionario, ordem=q)
            # Para cada opção que a gente tem de cada questão
            for opc in opcoes:
                # Gera o name igual lá no template
                name = f"opc_{q}_{opc}"
                opcao = Opcao.objects.get(questao=questao, ordem=opc)

                # pega o valor desse input que ficou selecionado no template
                valor = self.request.POST.get(name)
                # Criar um objeto Resposta para cada um com a tentativa, teste, opção, etc

                resp = Resposta.objects.create(
                    tentativa=tentativa, opcao=opcao, valor=valor)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['teste'] = get_object_or_404(Teste, pk=self.kwargs['pk_teste'], chave_acesso=self.kwargs['chave'], ativo=True)

        context['questionario'] = Questionario.objects.get(pk=1)

        context['questoes'] = Questao.objects.filter(
            questionario=context['questionario'])

        context['opcoes'] = {}

        for q in context['questoes']:
            context['opcoes'][q.pk] = Opcao.objects.filter(questao=q)

        return context


class RespostaView(TemplateView):
    template_name = 'resposta.html'
    # success_url = reverse_lazy("index")
    # model = Questionario

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Tentativa, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionario'] = Questionario.objects.get(pk=1)
        #teste = Teste.objects.get(pk=1)

        # Esse context é um objeto por causa do get
        context['tentativas'] = Tentativa.objects.filter(
            usuario=self.request.user).last()

        # Para o relatório do professor como DETAILVIEW de tentativa
        # context['tentativas'] = Tentativa.objects.get(pk=self.object.pk, teste__professor=self.request.user)

        # Filtra (gera uma lista) de respostas daquele objeto tentativa
        context['respostas'] = Resposta.objects.filter(
            tentativa=context['tentativas'])
        # for t in context['tentativas']:
        #    context['respostas'][t.pk] = Resposta.objects.filter(tentativa=t)

        # aqui vai calcular a quantidade de cada forma de aprendizagem traz

        context['EC'] = context['respostas'].filter(
            opcao__forma_aprendizagem__nome='Experiência Concreta').aggregate(Sum('valor'))
        context['OR'] = context['respostas'].filter(
            opcao__forma_aprendizagem__nome='Observação Reflexiva').aggregate(Sum('valor'))
        context['CA'] = context['respostas'].filter(
            opcao__forma_aprendizagem__nome='Conceituação Abstrato').aggregate(Sum('valor'))
        context['EA'] = context['respostas'].filter(
            opcao__forma_aprendizagem__nome='Experimentação Ativa').aggregate(Sum('valor'))

        EC = int(context['EC'].get('valor__sum'))
        OR = int(context['OR'].get('valor__sum'))
        CA = int(context['CA'].get('valor__sum'))
        EA = int(context['EA'].get('valor__sum'))

        context['EC'] = EC
        context['OR'] = OR
        context['CA'] = CA
        context['EA'] = EA

        # aqui calculo do resultado do estilo de aprendizagem

        assimilador = OR + CA
        convergente = CA + EA
        divergente = EC + OR
        acomodador = EA + EC
        resultadoSoma = max(assimilador, convergente, divergente, acomodador)

        context['resultadoSoma'] = resultadoSoma

        # função para descobrir o estilo
        estilos = Estilo.objects.all()
        if (resultadoSoma == divergente):
            estilo = Estilo.objects.get(id=2)
        if (resultadoSoma == assimilador):
            estilo = Estilo.objects.get(id=4)
        if (resultadoSoma == convergente):
            estilo = Estilo.objects.get(id=3)
        if (resultadoSoma == acomodador):
            estilo = Estilo.objects.get(id=1)

        context['estilo'] = estilo

        # aqui calcula o resultado da forma de aprendizagem

        eap1 = CA - EC  # +abstrato ou -concreto
        eap2 = EA - OR  # +ativo ou -reflexivo

        forma1 = FormaAprendizagem.objects.get(id=1)
        forma2 = FormaAprendizagem.objects.get(id=2)
        if (eap1 > 0):
            forma1 = FormaAprendizagem.objects.get(id=3)
        if (eap2 > 0):
            forma2 = FormaAprendizagem.objects.get(id=4)

        context['forma1'] = forma1
        context['forma2'] = forma2

        context['desc_estilo'] = estilo.descricao + \
            forma1.descricao + forma2.descricao
        context['rec_estilo'] = estilo.recomendacao + \
            forma1.recomendacao + forma2.recomendacao

        return context
