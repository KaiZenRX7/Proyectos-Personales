# Generated by Django 5.1.2 on 2024-11-17 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_entrenador_pokemons_alter_entrenador_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]
