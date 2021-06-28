from django.contrib import admin
from .models import Questionario, Questao, Teste, Tentativa, Opcao, Resposta, Estilo, FormaAprendizagem

# Register your models here.


@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')


@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'professor', 'questionario',
                    'turma', 'data', 'hora', 'chave_acesso', 'ativo')


@admin.register(Tentativa)
class TentativaAdmin(admin.ModelAdmin):
    list_display = ('id', 'teste', 'aluno', 'data', 'concluiu')


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'questionario', 'descricao', 'ordem')


@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'questao', 'descricao', 'imagem', 'video', 'ordem')


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tentativa', 'opcao', 'valor', 'aluno')


@admin.register(Estilo)
class EstiloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'recomendacao')


@admin.register(FormaAprendizagem)
class FormaAprendizagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'recomendacao')
