from django import template
from KolbStyleTeste.models import Resposta, Opcao, Questao

register = template.Library()

# Recebe uma lista e a posição que quer retornar dela


@register.filter(name='get_opcoes_questao')
def get_opcoes_questao(lista, id):
    return lista[id]


"""
@register.filter(name='avaliar_tentativa_kolb')
def avaliar_tentativa_kolb(lista):
    # print(lista)
    #respostas = Resposta.objects.filter(tentativa=tentativa)
    EC = 0
    OR = 0
    CA = 0
    EA = 0
    for res in lista:
        print('Questao:', res.opcao.questao.ordem)
        print('Opção:', res.opcao.ordem)
        # calculo EC
        if (res.opcao.questao.ordem == 1) and (res.opcao.ordem == 1):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 2) and (res.opcao.ordem == 3):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 3) and (res.opcao.ordem == 4):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 4) and (res.opcao.ordem == 1):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 5) and (res.opcao.ordem == 1):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 6) and (res.opcao.ordem == 3):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 7) and (res.opcao.ordem == 2):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 8) and (res.opcao.ordem == 4):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 9) and (res.opcao.ordem == 2):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 10) and (res.opcao.ordem == 2):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 11) and (res.opcao.ordem == 1):
            EC = res.valor + EC
        if (res.opcao.questao.ordem == 12) and (res.opcao.ordem == 2):
            EC = res.valor + EC
        # calculo OR
        if (res.opcao.questao.ordem == 1) and (res.opcao.ordem == 4):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 2) and (res.opcao.ordem == 1):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 3) and (res.opcao.ordem == 3):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 4) and (res.opcao.ordem == 3):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 5) and (res.opcao.ordem == 2):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 6) and (res.opcao.ordem == 1):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 7) and (res.opcao.ordem == 1):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 8) and (res.opcao.ordem == 3):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 9) and (res.opcao.ordem == 1):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 10) and (res.opcao.ordem == 1):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 11) and (res.opcao.ordem == 2):
            OR = res.valor + OR
        if (res.opcao.questao.ordem == 12) and (res.opcao.ordem == 3):
            OR = res.valor + OR
        # calculo CA
        if (res.opcao.questao.ordem == 1) and (res.opcao.ordem == 2):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 2) and (res.opcao.ordem == 2):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 3) and (res.opcao.ordem == 1):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 4) and (res.opcao.ordem == 4):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 5) and (res.opcao.ordem == 3):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 6) and (res.opcao.ordem == 4):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 7) and (res.opcao.ordem == 3):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 8) and (res.opcao.ordem == 2):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 9) and (res.opcao.ordem == 4):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 10) and (res.opcao.ordem == 4):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 11) and (res.opcao.ordem == 3):
            CA = res.valor + CA
        if (res.opcao.questao.ordem == 12) and (res.opcao.ordem == 1):
            CA = res.valor + CA
        # calculo EA
        if (res.opcao.questao.ordem == 1) and (res.opcao.ordem == 3):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 2) and (res.opcao.ordem == 4):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 3) and (res.opcao.ordem == 2):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 4) and (res.opcao.ordem == 2):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 5) and (res.opcao.ordem == 4):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 6) and (res.opcao.ordem == 2):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 7) and (res.opcao.ordem == 4):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 8) and (res.opcao.ordem == 1):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 9) and (res.opcao.ordem == 3):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 10) and (res.opcao.ordem == 3):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 11) and (res.opcao.ordem == 4):
            EA = res.valor + EA
        if (res.opcao.questao.ordem == 12) and (res.opcao.ordem == 4):
            EA = res.valor + EA

    print('EC', EC)
    print('OR', OR)
    print('CA', CA)
    print('EA', EA)

    assimilador = 0
    convergente = 0
    adaptador = 0
    acomodador = 0
    resultadoSomas = 0

    # calculo resultado

    return lista
"""
