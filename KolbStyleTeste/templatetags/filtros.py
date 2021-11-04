from django import template

register = template.Library()

# Recebe uma lista e a posição que quer retornar dela


@register.filter(name='get_dict_pos')
def get_dict_pos(lista, id):
    return lista[id]
