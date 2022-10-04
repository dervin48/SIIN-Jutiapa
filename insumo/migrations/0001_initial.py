# Generated by Django 4.1.1 on 2022-09-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id_insumo', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID Insumo')),
                ('nombre_insumo', models.CharField(max_length=50, verbose_name='Nombre Insumo')),
                ('unidad', models.CharField(max_length=50, verbose_name='Unidad de Medida')),
                ('precio', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos ',
                'db_table': 'insumo',
            },
        ),
    ]
