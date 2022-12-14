# Generated by Django 4.1.1 on 2022-09-24 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('nombre', models.CharField(max_length=50, verbose_name='nombres')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellidos')),
                ('cargo', models.CharField(max_length=30, verbose_name='cargo')),
                ('id_solicitante', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('fecha_iniciolabores', models.DateField(verbose_name='fecha inicio labores')),
            ],
            options={
                'verbose_name': 'Solicitante',
                'verbose_name_plural': 'Solicitantes',
                'db_table': 'solicitante',
            },
        ),
    ]
