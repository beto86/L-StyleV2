# Generated by Django 3.2.4 on 2021-06-26 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_delete_perfil'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='nome_cmpleto',
        ),
        migrations.AddField(
            model_name='perfil',
            name='nome_completo',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='cadastros.endereco', verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Prefiro_nao_opinar', 'Prefiro não opinar')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
