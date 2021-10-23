from django.db import models
from django.contrib.auth.models import User, Group
from cadastros.models import Turma

# Create your models here.


class Pais(models.Model):
    nome = models.CharField(max_length=60)
    nome_pt = models.CharField(max_length=60, verbose_name='nome')
    sigla = models.CharField(max_length=3)
    bacen = models.IntegerField()

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=60)
    uf = models.CharField(max_length=2, verbose_name='UF')
    ibge = models.IntegerField()
    pais = models.OneToOneField(Pais, on_delete=models.CASCADE, unique=False)
    ddd = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=120)
    uf = models.OneToOneField(Estado, on_delete=models.CASCADE, unique=False)
    ibge = models.IntegerField()

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    sexo_choice = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Prefiro_nao_opinar', 'Prefiro não opinar'),
    )
    nome_completo = models.CharField(
        max_length=50, null=True, verbose_name='Nome Completo')
    ra = models.CharField(max_length=10, unique=True,
                          verbose_name='RA', null=True)
    turma = models.ManyToManyField(Turma)
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF')
    telefone = models.CharField(max_length=16, null=True)
    sexo = models.CharField(max_length=30, choices=sexo_choice, null=True)
    data_nascimento = models.DateField(
        blank=True, null=True, verbose_name='Data de Nascimento')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # grupo = models.ForeignKey(
    # Group, on_delete=models.CASCADE, null=True)
    endereco = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Endereço')
    numero = models.CharField(max_length=10, blank=True, null=True,
                              verbose_name='Número')
    cep = models.CharField(max_length=45, blank=True,
                           null=True, verbose_name='CEP')
    cidade = models.ForeignKey(
        Cidade, blank=True, null=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(
        Estado, blank=True, null=True, on_delete=models.CASCADE)
    pais = models.ForeignKey(
        Pais, blank=True, null=True, on_delete=models.CASCADE, verbose_name='País')
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criação')
    atualizacao = models.DateTimeField(
        auto_now=True, verbose_name='Atualização')

    class Meta:
        verbose_name = 'Perfil'

    def __str__(self):
        return self.nome_completo
