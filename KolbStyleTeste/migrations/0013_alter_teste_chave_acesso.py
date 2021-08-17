# Generated by Django 3.2.5 on 2021-08-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KolbStyleTeste', '0012_auto_20210817_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='chave_acesso',
            field=models.CharField(default=123, help_text='Informe uma chave de acesso que também deverá ser fornecida aos usuários que irão responder o teste criado por você.', max_length=30, verbose_name='Chave de Acesso'),
            preserve_default=False,
        ),
    ]
