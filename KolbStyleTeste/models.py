from django.db import models
from django.contrib.auth.models import User
from cadastros.models import Turma
from usuarios.models import Perfil

# Create your models here.


class Estilo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=800, verbose_name='Descrição')
    recomendacao = models.TextField(
        max_length=500, verbose_name='Recomendação', blank=True, null=True)

    class Meta:
        verbose_name = 'Estilo'

    def __str__(self):
        return self.nome


class FormaAprendizagem(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(
        max_length=300, verbose_name='Descrição', blank=True, null=True)
    recomendacao = models.TextField(
        max_length=300, verbose_name='Recomendação', blank=True, null=True)

    class Meta:
        verbose_name = 'Forma de Aprendizagem'
        verbose_name_plural = 'Formas de Aprendizagens'

    def __str__(self):
        return self.nome


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
    chave_acesso = models.CharField(max_length=30, verbose_name='Chave de Acesso', unique=True,
                                    help_text='Informe uma chave de acesso que também deverá ser fornecida aos usuários que irão responder o teste criado por você.')
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Teste'

    def __str__(self):
        return self.descricao


class Tentativa(models.Model):
    teste = models.ForeignKey(
        Teste, related_name='testes', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    turma = models.ForeignKey(
        Turma, on_delete=models.CASCADE, blank=True, null=True)
    estilo = models.ForeignKey(
        Estilo, on_delete=models.CASCADE, blank=True, null=True)
    perfil = models.ForeignKey(
        Perfil, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Tentativa'

    def __str__(self):
        return f'{self.pk}-{self.teste.descricao}'


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
        return f'{self.ordem} - {self.descricao}'


class Opcao(models.Model):
    questao = models.ForeignKey(
        Questao, related_name='questaos', on_delete=models.CASCADE, verbose_name='Questão')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    img = models.CharField(max_length=100, null=True, blank=True)
    ordem = models.IntegerField()
    forma_aprendizagem = models.ForeignKey(FormaAprendizagem, on_delete=models.PROTECT,
                                           help_text="As respostas dessa opção serão somadas para calcular o valor da forma de aprendizagem selecionada.")

    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
        unique_together = ('ordem', 'questao')
        ordering = ['ordem']

    def __str__(self):
        return f'{self.ordem}-{self.descricao}'


class Resposta(models.Model):
    tentativa = models.ForeignKey(
        Tentativa, verbose_name='tentativas', on_delete=models.CASCADE)
    opcao = models.ForeignKey(
        Opcao, related_name='opcaos', on_delete=models.CASCADE, verbose_name='Opção')
    valor = models.IntegerField(default=0, null=True)

    class Meta:
        verbose_name = 'Resposta'

    def __str__(self):
        return self.opcao.descricao
