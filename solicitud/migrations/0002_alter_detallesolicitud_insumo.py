# Generated by Django 4.1.1 on 2022-09-24 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insumo', '0003_alter_insumo_existencia'),
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallesolicitud',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumo.insumo', verbose_name='Nombre Insumo'),
        ),
    ]
