from django.contrib import admin
from .models import Instituicao, Turma

# Register your models here.
"""
admin.site.register(Endereco)
admin.site.register(Estilo)
admin.site.register(FormaAprendizagem)
admin.site.register(Instituicao)
admin.site.register(Opcao)
admin.site.register(Perfil)
admin.site.register(Questao)
admin.site.register(Questionario)
admin.site.register(Resposta)
admin.site.register(Tentativa)
admin.site.register(Teste)
admin.site.register(Turma)
"""


@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'usuario')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'periodo', 'ano',
                    'curso', 'turno', 'instituicao', 'usuario')
