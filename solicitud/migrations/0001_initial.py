# Generated by Django 4.1.1 on 2022-09-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insumo', '0003_alter_insumo_existencia'),
        ('servicio', '0002_alter_servicio_descripcion'),
        ('solicitante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('requisicion', models.IntegerField(verbose_name='No Requiscion')),
                ('fecha_solicitud', models.DateField(verbose_name='Fecha Solicitud')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.servicio', verbose_name='Servicio')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitante.solicitante', verbose_name='Solicitante')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
                'db_table': 'solicitud',
            },
        ),
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(help_text='solo incluir numeros', verbose_name='Cantidad')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumo.insumo', verbose_name='nombre_insumo')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitud', verbose_name='Solicitud')),
            ],
        ),
    ]
