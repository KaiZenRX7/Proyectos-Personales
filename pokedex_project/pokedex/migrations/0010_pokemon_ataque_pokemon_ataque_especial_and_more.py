# Generated by Django 5.1.2 on 2024-11-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0009_entrenador_es_ficticio_alter_entrenador_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='ataque',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='ataque_especial',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='defensa',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='defensa_especial',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='velocidad',
            field=models.IntegerField(default=0),
        ),
    ]
