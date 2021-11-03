from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import DetailView
from KolbStyleTeste.models import Resposta, Questionario, Tentativa, Estilo, FormaAprendizagem, Turma, Teste
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from cadastros.models import Curso

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
    template_name = 'relatorio-turma.html'
    group_required = [u"Administrador", u"Professor"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # aqui traz todas turmas do usuario logado
        turmas = Turma.objects.filter(usuario=self.request.user)
        context['turmas'] = turmas

        # pega o id da tentativa selecionada do comboBox
        turma_id = self.request.GET.get("turmas")

        # Verifica se tem uma turma para consulta
        if(turma_id is not None):

            # Pesquisa a turma com esse ID que seja desse usuário
            turma = Turma.objects.get(pk=turma_id, usuario=self.request.user)
            context['turma'] = turma

            mediaTurma = {}

            testes = Teste.objects.filter(
                turma=turma, professor=self.request.user)
            context['testes'] = testes

            ##################
            # variaveis para calculo evolução do curso
            evlAcoJan = 0
            evlAcoFev = 0
            evlAcoMar = 0
            evlAcoAbr = 0
            evlAcoMai = 0
            evlAcoJun = 0
            evlAcoJul = 0
            evlAcoAgo = 0
            evlAcoSet = 0
            evlAcoNov = 0
            evlAcoDez = 0
            # # ASSIMILADOR
            evlAssJan = 0
            evlAssFev = 0
            evlAssMar = 0
            evlAssAbr = 0
            evlAssMai = 0
            evlAssJun = 0
            evlAssJul = 0
            evlAssAgo = 0
            evlAssSet = 0
            assimilador = 0
            evlAssNov = 0
            evlAssDez = 0
            # # CONVERGENTE
            evlConJan = 0
            evlConFev = 0
            evlConMar = 0
            evlConAbr = 0
            evlConMai = 0
            evlConJun = 0
            evlConJul = 0
            evlConAgo = 0
            evlConSet = 0
            evlConNov = 0
            evlConDez = 0
            # # CONVERGENTE
            evlDivJan = 0
            evlDivFev = 0
            evlDivMar = 0
            evlDivAbr = 0
            evlDivMai = 0
            evlDivJun = 0
            evlDivJul = 0
            evlDivAgo = 0
            evlDivSet = 0
            evlDivNov = 0
            evlDivDez = 0
            acomodador = 0
            assimilador = 0
            convergente = 0
            divergente = 0

            for t in testes:
                tentativas = Tentativa.objects.filter(teste=t)

                # aqui conta os estilos de cada turma
                mediaTurma[t.pk] = {
                    'tentativas': tentativas,
                    'Acomodador': tentativas.filter(estilo__nome='Acomodador').count(),
                    'Assimilador': tentativas.filter(estilo__nome='Assimilador').count(),
                    'Convergente': tentativas.filter(estilo__nome='Convergente').count(),
                    'Divergente': tentativas.filter(estilo__nome='Divergente').count(),

                }

                # para o grafico da evolução
                # para o mes de Janeiro
                evlAcoJan = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='01').count() + evlAcoJan
                evlAssJan = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='01').count() + evlAssJan
                evlConJan = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='01').count() + evlConJan
                evlDivJan = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='01').count() + evlDivJan

                # para o mes de Fevereiro
                evlAcoFev = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='02').count() + evlAcoFev
                evlAssFev = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='02').count() + evlAssFev
                evlConFev = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='02').count() + evlConFev
                evlDivFev = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='02').count() + evlDivFev

                # para o mes de Março
                evlAcoMar = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='03').count() + evlAcoMar
                evlAssMar = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='03').count() + evlAssMar
                evlConMar = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='03').count() + evlConMar
                evlDivMar = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='03').count() + evlDivMar

                # para o mes de Abril
                evlAcoAbr = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='04').count() + evlAcoAbr
                evlAssAbr = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='04').count() + evlAssAbr
                evlConAbr = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='04').count() + evlConAbr
                evlDivAbr = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='04').count() + evlDivAbr

                # para o mes de Maio
                evlAcoMai = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='05').count() + evlAcoMai
                evlAssMai = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='05').count() + evlAssMai
                evlConMai = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='05').count() + evlConMai
                evlDivMai = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='05').count() + evlDivMai

                # para o mes de Junho
                evlAcoJun = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='06').count() + evlAcoJun
                evlAssJun = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='06').count() + evlAssJun
                evlConJun = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='06').count() + evlConJun
                evlDivJun = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='06').count() + evlDivJun

                # para o mes de Julho
                evlAcoJul = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='07').count() + evlAcoJul
                evlAssJul = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='07').count() + evlAssJul
                evlConJul = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='07').count() + evlConJul
                evlDivJul = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='07').count() + evlDivJul

                # para o mes de Agosto
                evlAcoAgo = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='08').count() + evlAcoAgo
                evlAssAgo = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='08').count() + evlAssAgo
                evlConAgo = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='08').count() + evlConAgo
                evlDivAgo = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='08').count() + evlDivAgo

                # para o mes de Setembro
                evlAcoSet = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='09').count() + evlAcoSet
                evlAssSet = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='09').count() + evlAssSet
                evlConSet = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='09').count() + evlConSet
                evlDivSet = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='09').count() + evlDivSet

                # para o mes de Outubro
                acomodador = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='10').count() + acomodador
                assimilador = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='10').count() + assimilador
                convergente = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='10').count() + convergente
                divergente = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='10').count() + divergente

                # para o mes de Novembro
                evlAcoNov = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='11').count() + evlAcoNov
                evlAssNov = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='11').count() + evlAssNov
                evlConNov = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='11').count() + evlConNov
                evlDivNov = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='11').count() + evlDivNov

                # para o mes de Dezembro
                evlAcoDez = tentativas.filter(
                    estilo__nome='Acomodador', turma=turma, data__month='12').count() + evlAcoDez
                evlAssDez = tentativas.filter(
                    estilo__nome='Assimilador', turma=turma, data__month='12').count() + evlAssDez
                evlConDez = tentativas.filter(
                    estilo__nome='Convergente', turma=turma, data__month='12').count() + evlConDez
                evlDivDez = tentativas.filter(
                    estilo__nome='Divergente', turma=turma, data__month='12').count() + evlDivDez

            context['mediaTurma'] = mediaTurma

            # ####################
            # # a evolução do curso para o grafico de linha
            # # ACOMODADOR
            context['evlAcoJan'] = evlAcoJan
            context['evlAcoFev'] = evlAcoFev
            context['evlAcoMar'] = evlAcoMar
            context['evlAcoAbr'] = evlAcoAbr
            context['evlAcoMai'] = evlAcoMai
            context['evlAcoJun'] = evlAcoJun
            context['evlAcoJul'] = evlAcoJul
            context['evlAcoAgo'] = evlAcoAgo
            context['evlAcoSet'] = evlAcoSet
            context['evlAcoOut'] = acomodador
            context['evlAcoNov'] = evlAcoNov
            context['evlAcoDez'] = evlAcoDez
            # # ASSIMILADOR
            context['evlAssJan'] = evlAssJan
            context['evlAssFev'] = evlAssFev
            context['evlAssMar'] = evlAssMar
            context['evlAssAbr'] = evlAssAbr
            context['evlAssMai'] = evlAssMai
            context['evlAssJun'] = evlAssJun
            context['evlAssJul'] = evlAssJul
            context['evlAssAgo'] = evlAssAgo
            context['evlAssSet'] = evlAssSet
            context['evlAssOut'] = assimilador
            context['evlAssNov'] = evlAssNov
            context['evlAssDez'] = evlAssDez
            # # CONVERGENTE
            context['evlConJan'] = evlConJan
            context['evlConFev'] = evlConFev
            context['evlConMar'] = evlConMar
            context['evlConAbr'] = evlConAbr
            context['evlConMai'] = evlConMai
            context['evlConJun'] = evlConJun
            context['evlConJul'] = evlConJul
            context['evlConAgo'] = evlConAgo
            context['evlConSet'] = evlConSet
            context['evlConOut'] = convergente
            context['evlConNov'] = evlConNov
            context['evlConDez'] = evlConDez
            # # CONVERGENTE
            context['evlDivJan'] = evlDivJan
            context['evlDivFev'] = evlDivFev
            context['evlDivMar'] = evlDivMar
            context['evlDivAbr'] = evlDivAbr
            context['evlDivMai'] = evlDivMai
            context['evlDivJun'] = evlDivJun
            context['evlDivJul'] = evlDivJul
            context['evlDivAgo'] = evlDivAgo
            context['evlDivSet'] = evlDivSet
            context['evlDivOut'] = divergente
            context['evlDivNov'] = evlDivNov
            context['evlDivDez'] = evlDivDez

        return context


class RelatorioCurso(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'relatorio-curso.html'
    group_required = [u"Administrador", u"Professor"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # aqui traz todos cursos do usuario logado
        cursos = Curso.objects.filter(usuario=self.request.user)
        context['cursos'] = cursos

        # pega o id da tentativa selecionada do comboBox
        curso_id = self.request.GET.get("cursos")

        # Verifica se tem um curso para consulta
        if(curso_id is not None):
            print("======================")
            print(curso_id)
            # Pesquisa a turma com esse ID que seja desse usuário
            curso = Curso.objects.get(
                pk=curso_id, usuario=self.request.user)
            # context['turma'] =

            mediaCurso = {}

            testes = Teste.objects.filter(
                turma__curso=curso, professor=self.request.user)
            context['testes'] = testes
            print("======================")
            print(testes)

            ##################
            # variaveis para calculo evolução do curso
            curAcoJan = 0
            curAcoFev = 0
            curAcoMar = 0
            curAcoAbr = 0
            curAcoMai = 0
            curAcoJun = 0
            curAcoJul = 0
            curAcoAgo = 0
            curAcoSet = 0
            curAcoNov = 0
            curAcoDez = 0
            # # ASSIMILADOR
            curAssJan = 0
            curAssFev = 0
            curAssMar = 0
            curAssAbr = 0
            curAssMai = 0
            curAssJun = 0
            curAssJul = 0
            curAssAgo = 0
            curAssSet = 0
            assimilador = 0
            curAssNov = 0
            curAssDez = 0
            # # CONVERGENTE
            curConJan = 0
            curConFev = 0
            curConMar = 0
            curConAbr = 0
            curConMai = 0
            curConJun = 0
            curConJul = 0
            curConAgo = 0
            curConSet = 0
            curConNov = 0
            curConDez = 0
            # # CONVERGENTE
            curDivJan = 0
            curDivFev = 0
            curDivMar = 0
            curDivAbr = 0
            curDivMai = 0
            curDivJun = 0
            curDivJul = 0
            curDivAgo = 0
            curDivSet = 0
            curDivNov = 0
            curDivDez = 0
            acomodador = 0
            assimilador = 0
            convergente = 0
            divergente = 0

            for t in testes:
                tentativas = Tentativa.objects.filter(teste=t)

                # aqui conta os estilos de cada turma
                mediaCurso[t.pk] = {
                    'tentativas': tentativas,
                    'Acomodador': tentativas.filter(estilo__nome='Acomodador').count(),
                    'Assimilador': tentativas.filter(estilo__nome='Assimilador').count(),
                    'Convergente': tentativas.filter(estilo__nome='Convergente').count(),
                    'Divergente': tentativas.filter(estilo__nome='Divergente').count(),
                }

                #  para o grafico da evolução
                # para o mes de Janeiro
                curAcoJan = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='01').count() + curAcoJan
                curAssJan = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='01').count() + curAssJan
                curConJan = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='01').count() + curConJan
                curDivJan = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='01').count() + curDivJan

                # para o mes de Fevereiro
                curAcoFev = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='02').count() + curAcoFev
                curAssFev = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='02').count() + curAssFev
                curConFev = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='02').count() + curConFev
                curDivFev = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='02').count() + curDivFev

                # para o mes de Março
                curAcoMar = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='03').count() + curAcoMar
                curAssMar = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='03').count() + curAssMar
                curConMar = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='03').count() + curConMar
                curDivMar = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='03').count() + curDivMar

                # para o mes de Abril
                curAcoAbr = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='04').count() + curAcoAbr
                curAssAbr = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='04').count() + curAssAbr
                curConAbr = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='04').count() + curConAbr
                curDivAbr = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='04').count() + curDivAbr

                # para o mes de Maio
                curAcoMai = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='05').count() + curAcoMai
                curAssMai = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='05').count() + curAssMai
                curConMai = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='05').count() + curConMai
                curDivMai = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='05').count() + curDivMai

                # para o mes de Junho
                curAcoJun = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='06').count() + curAcoJun
                curAssJun = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='06').count() + curAssJun
                curConJun = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='06').count() + curConJun
                curDivJun = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='06').count() + curDivJun

                # para o mes de Julho
                curAcoJul = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='07').count() + curAcoJul
                curAssJul = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='07').count() + curAssJul
                curConJul = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='07').count() + curConJul
                curDivJul = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='07').count() + curDivJul

                # para o mes de Agosto
                curAcoAgo = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='08').count() + curAcoAgo
                curAssAgo = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='08').count() + curAssAgo
                curConAgo = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='08').count() + curConAgo
                curDivAgo = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='08').count() + curDivAgo

                # para o mes de Setembro
                curAcoSet = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='09').count() + curAcoSet
                curAssSet = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='09').count() + curAssSet
                curConSet = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='09').count() + curConSet
                curDivSet = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='09').count() + curDivSet

                # para o mes de Outubro
                acomodador = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='10').count() + acomodador
                assimilador = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='10').count() + assimilador
                convergente = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='10').count() + convergente
                divergente = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='10').count() + divergente

                # para o mes de Novembro
                curAcoNov = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='11').count() + curAcoNov
                curAssNov = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='11').count() + curAssNov
                curConNov = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='11').count() + curConNov
                curDivNov = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='11').count() + curDivNov

                # para o mes de Dezembro
                curAcoDez = tentativas.filter(
                    estilo__nome='Acomodador', turma__curso=curso, data__month='12').count() + curAcoDez
                curAssDez = tentativas.filter(
                    estilo__nome='Assimilador', turma__curso=curso, data__month='12').count() + curAssDez
                curConDez = tentativas.filter(
                    estilo__nome='Convergente', turma__curso=curso, data__month='12').count() + curConDez
                curDivDez = tentativas.filter(
                    estilo__nome='Divergente', turma__curso=curso, data__month='12').count() + curDivDez

            context['mediaCurso'] = mediaCurso

            # ####################
            # # a evolução do curso para o grafico de linha
            # # ACOMODADOR
            context['curAcoJan'] = curAcoJan
            context['curAcoFev'] = curAcoFev
            context['curAcoMar'] = curAcoMar
            context['curAcoAbr'] = curAcoAbr
            context['curAcoMai'] = curAcoMai
            context['curAcoJun'] = curAcoJun
            context['curAcoJul'] = curAcoJul
            context['curAcoAgo'] = curAcoAgo
            context['curAcoSet'] = curAcoSet
            context['curAcoOut'] = acomodador
            context['curAcoNov'] = curAcoNov
            context['curAcoDez'] = curAcoDez
            # # ASSIMILADOR
            context['curAssJan'] = curAssJan
            context['curAssFev'] = curAssFev
            context['curAssMar'] = curAssMar
            context['curAssAbr'] = curAssAbr
            context['curAssMai'] = curAssMai
            context['curAssJun'] = curAssJun
            context['curAssJul'] = curAssJul
            context['curAssAgo'] = curAssAgo
            context['curAssSet'] = curAssSet
            context['curAssOut'] = assimilador
            context['curAssNov'] = curAssNov
            context['curAssDez'] = curAssDez
            # # CONVERGENTE
            context['curConJan'] = curConJan
            context['curConFev'] = curConFev
            context['curConMar'] = curConMar
            context['curConAbr'] = curConAbr
            context['curConMai'] = curConMai
            context['curConJun'] = curConJun
            context['curConJul'] = curConJul
            context['curConAgo'] = curConAgo
            context['curConSet'] = curConSet
            context['curConOut'] = convergente
            context['curConNov'] = curConNov
            context['curConDez'] = curConDez
            # # CONVERGENTE
            context['curDivJan'] = curDivJan
            context['curDivFev'] = curDivFev
            context['curDivMar'] = curDivMar
            context['curDivAbr'] = curDivAbr
            context['curDivMai'] = curDivMai
            context['curDivJun'] = curDivJun
            context['curDivJul'] = curDivJul
            context['curDivAgo'] = curDivAgo
            context['curDivSet'] = curDivSet
            context['curDivOut'] = divergente
            context['curDivNov'] = curDivNov
            context['curDivDez'] = curDivDez

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
