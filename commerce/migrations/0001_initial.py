# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_id', models.IntegerField(serialize=False, primary_key=True, db_column='CLI_ID')),
                ('cli_dni', models.CharField(max_length=8, unique=True, null=True, db_column='CLI_DNI', blank=True)),
                ('cli_nombres', models.CharField(max_length=70, db_column='CLI_NOMBRES')),
                ('cli_appaterno', models.CharField(max_length=45, db_column='CLI_APPATERNO')),
                ('cli_apmaterno', models.CharField(max_length=45, null=True, db_column='CLI_APMATERNO', blank=True)),
                ('cli_direcion', models.CharField(max_length=90, null=True, db_column='CLI_DIRECION', blank=True)),
                ('cli_celular', models.CharField(max_length=9, null=True, db_column='CLI_CELULAR', blank=True)),
                ('cli_email', models.CharField(max_length=70, null=True, db_column='CLI_EMAIL', blank=True)),
                ('cli_nac', models.DateField(null=True, db_column='CLI_NAC', blank=True)),
            ],
            options={
                'db_table': 'CLIENTE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('est_id', models.IntegerField(serialize=False, primary_key=True, db_column='EST_ID')),
                ('est_nombre', models.CharField(max_length=70, db_column='EST_NOMBRE')),
                ('est_desc', models.CharField(max_length=200, null=True, db_column='EST_DESC', blank=True)),
            ],
            options={
                'db_table': 'ESTADO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('men_id', models.IntegerField(serialize=False, primary_key=True, db_column='MEN_ID')),
                ('men_nombre', models.CharField(max_length=45, db_column='MEN_NOMBRE')),
                ('men_contenido', models.CharField(max_length=400, db_column='MEN_CONTENIDO')),
                ('men_fechae', models.DateField(db_column='MEN_FECHAE')),
            ],
            options={
                'db_table': 'MENSAJE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('pago_id', models.IntegerField(serialize=False, primary_key=True, db_column='PAGO_ID')),
                ('pago_cuentadm', models.CharField(max_length=9, db_column='PAGO_CUENTADM')),
                ('pago_monto', models.DecimalField(decimal_places=0, max_digits=10, db_column='PAGO_MONTO')),
                ('pago_fecha', models.DateTimeField(db_column='PAGO_FECHA')),
            ],
            options={
                'db_table': 'PAGO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('res_id', models.IntegerField(serialize=False, primary_key=True, db_column='RES_ID')),
                ('res_fecha', models.DateTimeField(db_column='RES_FECHA')),
                ('res_cuentadm', models.CharField(max_length=45, null=True, db_column='RES_CUENTADM', blank=True)),
                ('res_detalles', models.CharField(max_length=45, null=True, db_column='RES_DETALLES', blank=True)),
            ],
            options={
                'db_table': 'RESERVA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.IntegerField(serialize=False, primary_key=True, db_column='ROL_ID')),
                ('rol_nombre', models.CharField(max_length=70, db_column='ROL_NOMBRE')),
                ('rol_desc', models.CharField(max_length=200, db_column='ROL_DESC')),
            ],
            options={
                'db_table': 'ROL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('tar_id', models.IntegerField(serialize=False, primary_key=True, db_column='TAR_ID')),
                ('tar_nombre', models.CharField(max_length=70, db_column='TAR_NOMBRE')),
                ('tar_desc', models.CharField(max_length=200, db_column='TAR_DESC')),
                ('tar_costo', models.DecimalField(decimal_places=0, max_digits=10, db_column='TAR_COSTO')),
            ],
            options={
                'db_table': 'TARIFA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('tipo_id', models.IntegerField(serialize=False, primary_key=True, db_column='TIPO_ID')),
                ('tipo_nombre', models.CharField(max_length=80, db_column='TIPO_NOMBRE')),
                ('tipo_des', models.CharField(max_length=300, null=True, db_column='TIPO_DES', blank=True)),
            ],
            options={
                'db_table': 'TIPO',
                'managed': False,
            },
        ),
    ]
