from django import template

register = template.Library()

# Recebe uma lista e a posição que quer retornar dela
@register.filter(name='get_opcoes_questao')
def get_opcoes_questao(lista, id):
    return lista[id]