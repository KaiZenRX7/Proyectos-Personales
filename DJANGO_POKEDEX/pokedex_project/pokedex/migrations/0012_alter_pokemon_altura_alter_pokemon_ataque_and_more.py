# Generated by Django 5.1.2 on 2024-11-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0011_pokemon_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='altura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='ataque',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='ataque_especial',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='defensa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='defensa_especial',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='evolucion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='velocidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
