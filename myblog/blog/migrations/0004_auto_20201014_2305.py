# Generated by Django 3.1.2 on 2020-10-14 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201014_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='data_evento',
            new_name='event_date',
        ),
    ]
