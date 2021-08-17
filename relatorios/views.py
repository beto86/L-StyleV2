from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import DetailView
from KolbStyleTeste.models import Resposta, Questionario, Tentativa, Estilo, FormaAprendizagem, Turma
from django.db.models import Sum

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
        context['respostas'] = Resposta.objects.filter(tentativa=context['tentativas'])
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
        #mediaTurma = Tentativa.objects.filter(teste)
        #context['mediaTurma'] = mediaTurma

        return context


class RelatorioTurma(TemplateView):
    template_name = 'relatorio.html'
