# Generated by Django 3.2.4 on 2021-08-15 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0006_alter_instituicao_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='usuario',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
