# Generated by Django 3.1.3 on 2020-11-19 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='created',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='updated',
            new_name='creado',
        ),
    ]