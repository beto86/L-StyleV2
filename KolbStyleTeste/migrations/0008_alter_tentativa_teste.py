# Generated by Django 3.2.4 on 2021-07-15 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KolbStyleTeste', '0007_alter_resposta_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tentativa',
            name='teste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testes', to='KolbStyleTeste.teste'),
        ),
    ]
