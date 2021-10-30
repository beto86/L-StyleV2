from django.contrib import admin
from .models import Instituicao, Turma, Curso


@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'usuario')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'periodo', 'ano',
                    'curso', 'turno', 'instituicao', 'usuario')


@admin.register(Curso)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'usuario')
