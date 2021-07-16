from django.db import models
from django.contrib.auth.models import User
from cadastros.models import Turma

# Create your models here.


class Questionario(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Questionário'

    def __str__(self):
        return self.descricao


class Teste(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descriçãos')
    professor = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    questionario = models.ForeignKey(
        Questionario, related_name='questionarios', on_delete=models.CASCADE)
    turma = models.ForeignKey(
        Turma, related_name='turmas', on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateField(auto_now_add=True)
    hora = models.DateTimeField(auto_now_add=True)
    chave_acesso = models.CharField(
        max_length=30, verbose_name='Chave de Acesso', blank=True, null=True)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Teste'

    def __str__(self):
        return self.descricao


class Tentativa(models.Model):
    teste = models.ForeignKey(
        Teste, related_name='testes', on_delete=models.CASCADE)
    aluno = models.ForeignKey(
        User, related_name='%(class)s_alunos', on_delete=models.PROTECT, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    # Remover atributo
    concluiu = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tentativa'

    def __str__(self):
        return self.teste.descricao


class Questao(models.Model):
    questionario = models.ForeignKey(
        Questionario, related_name='%(class)s_questionarios', on_delete=models.CASCADE, null=True)
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    ordem = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        # para não repetir ordem das questões
        unique_together = ('questionario', 'ordem')
        ordering = ['ordem']

    def __str__(self):
        return self.descricao


class Opcao(models.Model):
    questao = models.ForeignKey(
        Questao, related_name='questaos', on_delete=models.CASCADE, verbose_name='Questão')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    imagem = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    ordem = models.IntegerField()

    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
        unique_together = ('ordem', 'questao')
        ordering = ['ordem']

    def __str__(self):
        return self.descricao


class Resposta(models.Model):
    tentativa = models.ForeignKey(
        Tentativa, verbose_name='tentativas', on_delete=models.CASCADE)
    opcao = models.ForeignKey(
        Opcao, related_name='opcaos', on_delete=models.CASCADE, verbose_name='Opção')
    valor = models.IntegerField(default=0, null=True)
    aluno = models.ForeignKey(
        User, related_name='alunos', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Resposta'

    def __str__(self):
        return self.opcao.descricao


class Estilo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=300, verbose_name='Descrição')
    recomendacao = models.TextField(
        max_length=300, verbose_name='Recomendação')

    class Meta:
        verbose_name = 'Estilo'

    def __str__(self):
        return self.nome


class FormaAprendizagem(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=300, verbose_name='Descrição')
    recomendacao = models.TextField(
        max_length=300, verbose_name='Recomendação')

    class Meta:
        verbose_name = 'Forma de Aprendizagem'
        verbose_name_plural = 'Formas de Aprendizagens'

    def __str__(self):
        return self.nome
