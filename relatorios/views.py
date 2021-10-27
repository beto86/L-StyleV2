from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import DetailView
from KolbStyleTeste.models import Resposta, Questionario, Tentativa, Estilo, FormaAprendizagem, Turma, Teste
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from easy_pdf.views import PDFTemplateResponseMixin

# Create your views here.


class RelatorioPorAlunoView(DetailView):
    template_name = "relatorio-aluno.html"
    model = Tentativa
    # success_url = reverse_lazy("index")

    def get_object(self):
        # Consultar o grupo do usuário, se for aluno faz isso...
        # return get_object_or_404(Tentativa, pk=self.kwargs.get("id"), usuario=self.request.user)
        return get_object_or_404(Tentativa, pk=self.kwargs["id"])
        # Se não for aluno
        # return get_object_or_404(Tentativa, pk=self.kwargs.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionario'] = Questionario.objects.get(pk=1)
        #teste = Teste.objects.get(pk=1)

        # Esse context é um objeto por causa do get
        # context['tentativas'] = Tentativa.objects.filter(aluno=self.request.user).last()

        # Para o relatório do professor como DETAILVIEW de tentativa
        context['tentativas'] = self.object

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

        ##############################
        # para a média da turma
        # pega o objeto tentativa de quem respondeu
        quem_respondeu = Tentativa.objects.get(pk=self.kwargs["id"])
        # aqui filtra de acordo com quem respondeu
        mediaTurma = Tentativa.objects.filter(usuario=quem_respondeu.usuario)
        context['mediaTurma'] = mediaTurma

        # aqui conta os estilos de cada turma
        context['Acomodador'] = context['mediaTurma'].filter(
            estilo__nome='Acomodador').count()
        context['Assimilador'] = context['mediaTurma'].filter(
            estilo__nome='Assimilador').count()
        context['Convergente'] = context['mediaTurma'].filter(
            estilo__nome='Convergente').count()
        context['Divergente'] = context['mediaTurma'].filter(
            estilo__nome='Divergente').count()

        ##########################################
        # para a lista das tentativas do aluno

        # pega o usuario da tentativa de quem respondeu
        context['quem_respondeu'] = quem_respondeu.usuario
        # aqui filtra de acordo com quem respondeu ordenado por data
        context['tentativa'] = mediaTurma.order_by('data')

        return context


class RelatorioTurma(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'relatorio.html'
    group_required = [u"Administrador", u"Professor"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # aqui traz todas turmas do usuario logado
        turmas = Turma.objects.filter(usuario=self.request.user)
        context['turmas'] = turmas

        # pega o id da tentativa selecionada do comboBox
        turma = self.request.GET.get("turmas")
        context['nome_turma'] = turma

        turma = Turma.objects.get(pk=turma, usuario=self.request.user)

        # fazer if se tem turma
        testes = Teste.objects.filter(turma=turma)

        tentativas = {}
        for t in testes:
            tentativas[t.pk] = Tentativa.objects.filter(teste=t)

        # aqui filtra a turma de acordo com o id
        mediaTurma = Tentativa.objects.filter(turma__nome=nome_turma)
        context['mediaTurma'] = mediaTurma

        # aqui conta os estilos de cada turma
        context['Acomodador'] = context['mediaTurma'].filter(
            estilo__nome='Acomodador').count()
        context['Assimilador'] = context['mediaTurma'].filter(
            estilo__nome='Assimilador').count()
        context['Convergente'] = context['mediaTurma'].filter(
            estilo__nome='Convergente').count()
        context['Divergente'] = context['mediaTurma'].filter(
            estilo__nome='Divergente').count()

        #################
        # usar este comando para popular o combobox de curso com postegres
        # cursos = Turma.objects.filter(
        #    usuario=self.request.user).values('curso').distinct('curso')
        queryset = Turma.objects.distinct()
        cursos = queryset.filter(
            usuario=self.request.user).values('curso')
        context['cursos'] = cursos

        # pega o id da tentativa selecionada do comboBox
        nome_turma_curso = self.request.GET.get("cursos")
        context['nome_turma_curso'] = nome_turma_curso

        # aqui filtra a turma de acordo com o curso
        mediaCurso = Tentativa.objects.filter(
            usuario=self.request.user, turma__curso=nome_turma_curso)
        context['mediaCurso'] = mediaCurso

        ####################
        # a evolução da turma para o grafico de linha
        # tenho que achar o filtro para data por mes
        # ACOMODADOR
        context['evlAcoJan'] = 0
        context['evlAcoFev'] = 0
        context['evlAcoMar'] = 0
        context['evlAcoAbr'] = 0
        context['evlAcoMai'] = 0
        context['evlAcoJun'] = 0
        context['evlAcoJul'] = 0
        context['evlAcoAgo'] = 0
        context['evlAcoSet'] = 0
        context['evlAcoOut'] = context['Acomodador']
        context['evlAcoNov'] = 0
        context['evlAcoDes'] = 0
        # ASSIMILADOR
        context['evlAssJan'] = 0
        context['evlAssFev'] = 0
        context['evlAssMar'] = 0
        context['evlAssAbr'] = 0
        context['evlAssMai'] = 0
        context['evlAssJun'] = 0
        context['evlAssJul'] = 0
        context['evlAssAgo'] = 0
        context['evlAssSet'] = 0
        context['evlAssOut'] = context['Assimilador']
        context['evlAssNov'] = 0
        context['evlAssDes'] = 0
        # CONVERGENTE
        context['evlConJan'] = 0
        context['evlConFev'] = 0
        context['evlConMar'] = 0
        context['evlConAbr'] = 0
        context['evlConMai'] = 0
        context['evlConJun'] = 0
        context['evlConJul'] = 0
        context['evlConAgo'] = 0
        context['evlConSet'] = 0
        context['evlConOut'] = context['Convergente']
        context['evlConNov'] = 0
        context['evlConDes'] = 0
        # CONVERGENTE
        context['evlDivJan'] = 0
        context['evlDivFev'] = 0
        context['evlDivMar'] = 0
        context['evlDivAbr'] = 0
        context['evlDivMai'] = 0
        context['evlDivJun'] = 0
        context['evlDivJul'] = 0
        context['evlDivAgo'] = 0
        context['evlDivSet'] = 0
        context['evlDivOut'] = context['Divergente']
        context['evlDivNov'] = 0
        context['evlDivDes'] = 0

        ################################################
        # relatorio do curso
        # aqui conta os estilos de cada curso
        context['AcomodadorCurso'] = context['mediaCurso'].filter(
            estilo__nome='Acomodador').count()
        context['AssimiladorCurso'] = context['mediaCurso'].filter(
            estilo__nome='Assimilador').count()
        context['ConvergenteCurso'] = context['mediaCurso'].filter(
            estilo__nome='Convergente').count()
        context['DivergenteCurso'] = context['mediaCurso'].filter(
            estilo__nome='Divergente').count()

        ####################
        # a evolução do curso para o grafico de linha
        # tenho que achar o filtro para data por mes
        # ACOMODADOR
        context['curAcoJan'] = 0
        context['curAcoFev'] = 0
        context['curAcoMar'] = 0
        context['curAcoAbr'] = 0
        context['curAcoMai'] = 0
        context['curAcoJun'] = 0
        context['curAcoJul'] = 0
        context['curAcoAgo'] = 0
        context['curAcoSet'] = 0
        context['curAcoOut'] = context['AcomodadorCurso']
        context['curAcoNov'] = 0
        context['curAcoDes'] = 0
        # ASSIMILADOR
        context['curAssJan'] = 0
        context['curAssFev'] = 0
        context['curAssMar'] = 0
        context['curAssAbr'] = 0
        context['curAssMai'] = 0
        context['curAssJun'] = 0
        context['curAssJul'] = 0
        context['curAssAgo'] = 0
        context['curAssSet'] = 0
        context['curAssOut'] = context['AssimiladorCurso']
        context['curAssNov'] = 0
        context['curAssDes'] = 0
        # CONVERGENTE
        context['curConJan'] = 0
        context['curConFev'] = 0
        context['curConMar'] = 0
        context['curConAbr'] = 0
        context['curConMai'] = 0
        context['curConJun'] = 0
        context['curConJul'] = 0
        context['curConAgo'] = 0
        context['curConSet'] = 0
        context['curConOut'] = context['ConvergenteCurso']
        context['curConNov'] = 0
        context['curConDes'] = 0
        # CONVERGENTE
        context['curDivJan'] = 0
        context['curDivFev'] = 0
        context['curDivMar'] = 0
        context['curDivAbr'] = 0
        context['curDivMai'] = 0
        context['curDivJun'] = 0
        context['curDivJul'] = 0
        context['curDivAgo'] = 0
        context['curDivSet'] = 0
        context['curDivOut'] = context['DivergenteCurso']
        context['curDivNov'] = 0
        context['curDivDes'] = 0

        ################################################
        # relatorio para a tabela da turma
        context['evlTurma'] = Tentativa.objects.filter(
            teste__professor=self.request.user).order_by('data')

        ################################################
        # relatorio para a tabela do curso
        context['evlCurso'] = Tentativa.objects.filter(
            usuario=self.request.user, turma__curso=nome_turma_curso).order_by('data')

        return context


class PDFAlunoDetailView(PDFTemplateResponseMixin, DetailView):
    model = Tentativa
    template_name = 'pdfAluno_detail.html'
    download_filename = 'relatorio-aluno.pdf'

    def get_object(self):
        # Consultar o grupo do usuário, se for aluno faz isso...
        # return get_object_or_404(Tentativa, pk=self.kwargs.get("id"), usuario=self.request.user)
        return get_object_or_404(Tentativa, pk=self.kwargs["id"])
        # Se não for aluno
        # return get_object_or_404(Tentativa, pk=self.kwargs.get("id"))

    def get_context_data(self, **kwargs):
        context = super(PDFAlunoDetailView, self).get_context_data(**kwargs)

        context['pagesize'] = "A4"
        context['encoding'] = u"utf-8"

        context['title'] = f'relatorio do aluno {self.request.user}'

        context['questionario'] = Questionario.objects.get(pk=1)
        #teste = Teste.objects.get(pk=1)
        # Esse context é um objeto por causa do get
        # context['tentativas'] = Tentativa.objects.filter(aluno=self.request.user).last()

        # Para o relatório do professor como DETAILVIEW de tentativa
        context['tentativas'] = self.object

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

        ##############################
        # para a média da turma
        # pega o objeto tentativa de quem respondeu
        quem_respondeu = Tentativa.objects.get(pk=self.kwargs["id"])
        # aqui filtra de acordo com quem respondeu
        mediaTurma = Tentativa.objects.filter(usuario=quem_respondeu.usuario)
        context['mediaTurma'] = mediaTurma

        ##########################################
        # para a lista das tentativas do aluno

        # pega o usuario da tentativa de quem respondeu
        context['quem_respondeu'] = quem_respondeu.usuario
        # aqui filtra de acordo com quem respondeu ordenado por data
        context['tentativa'] = mediaTurma.order_by('data')

        return context
