# Generated by Django 3.1.2 on 2020-10-14 23:02

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('encerrado', 'Encerrado'), ('aguardando', 'Aguardando')], max_length=15)),
                ('title', models.CharField(max_length=255)),
                ('data_evento', models.DateTimeField()),
                ('author', models.CharField(max_length=255, verbose_name=django.contrib.auth.models.User)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
