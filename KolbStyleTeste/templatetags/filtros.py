from django import template
from KolbStyleTeste.models import Resposta

register = template.Library()

# Recebe uma lista e a posição que quer retornar dela


@register.filter(name='get_opcoes_questao')
def get_opcoes_questao(lista, id):
    return lista[id]


@register.filter(name='avaliar_tentativa_kolb')
def avaliar_tentativa_kolb(tentativa):
    respostas = Resposta.objects.filter(tentativa=tentativa)

    # cálculos do teste

    # calculo EC
    # 1a

    return 'ok'
