from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Endereco(models.Model):
    cep = models.CharField(max_length=45, verbose_name='CEP')
    rua = models.CharField(max_length=45)
    numero = models.IntegerField(verbose_name='Número')
    complemento = models.CharField(max_length=45, blank=True, null=True)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Endereço'

    def __str__(self):
        return f'{self.rua}, {self.numero}, {self.cidade}'


class Perfil(models.Model):
    sexo_choice = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Prefiro_nao_opinar', 'Prefiro não opinar'),
    )
    sexo = models.CharField(max_length=30, choices=sexo_choice,
                            default='Prefiro_nao_opinar', blank=True, null=True)
    data_nascimento = models.DateField(
        blank=True, null=True, verbose_name='Data de Nascimento')
    fone = models.CharField(max_length=12, blank=True,
                            null=True, verbose_name='Telefone')
    email = models.EmailField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='enderecos',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='Endereço')
    cpf = models.CharField(max_length=12, blank=True,
                           null=True, verbose_name='CPF')
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criação')
    atualizacao = models.DateTimeField(
        auto_now=True, verbose_name='Atualização')

    class Meta:
        verbose_name = 'Perfil'

    def __str__(self):
        return self.cpf


class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, related_name='%(class)s_enderecos',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='Endereço')

    class Meta:
        verbose_name = 'Instituição de Ensino'

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=45)
    ra = models.CharField(max_length=10, unique=True, verbose_name='RA')
    periodo = models.IntegerField(verbose_name='Período')
    ano = models.IntegerField()
    curso = models.CharField(max_length=45)
    turno = models.CharField(max_length=15, blank=True, null=True)
    instituicao = models.ForeignKey(
        Instituicao, related_name='instituicao_ensinos', on_delete=models.CASCADE, verbose_name='Instituição de Ensino', blank=True, null=True)

    class Meta:
        verbose_name = 'Turma'

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
    chave_acesso = models.CharField(
        max_length=30, verbose_name='Chave de Acesso', blank=True, null=True)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Teste'

    def __str__(self):
        return self.descricao


class Tentativa(models.Model):
    teste = models.OneToOneField(
        Teste, related_name='testes', on_delete=models.CASCADE)
    aluno = models.ForeignKey(
        User, related_name='%(class)s_alunos', on_delete=models.PROTECT, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    concluiu = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tentativa'

    def __str__(self):
        return self.teste.descricao


class Questao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Questão'

    def __str__(self):
        return self.descricao


class Opcao(models.Model):
    questao = models.ForeignKey(
        Questao, related_name='questaos', on_delete=models.CASCADE, verbose_name='Questão')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    ordem = models.IntegerField()

    class Meta:
        verbose_name = 'Opção'
        unique_together = ('descricao', 'questao')

    def __str__(self):
        return self.descricao


class Resposta(models.Model):
    tentativa = models.OneToOneField(
        Tentativa, verbose_name='tentativas', on_delete=models.CASCADE)
    opcao = models.ForeignKey(
        Opcao, related_name='opcaos', on_delete=models.CASCADE, verbose_name='Opção')
    valor = models.IntegerField()
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
        verbose_name = 'Estilo'

    def __str__(self):
        return self.nome
