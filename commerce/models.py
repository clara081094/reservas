from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(models.Model):
    cli_id = models.AutoField(db_column='CLI_ID', primary_key=True)  # Field name made lowercase.
    cli_dni = models.CharField(db_column='CLI_DNI', unique=True, max_length=8, blank=True, null=True)  # Field name made lowercase.
    cli_nombres = models.CharField(db_column='CLI_NOMBRES', max_length=70)  # Field name made lowercase.
    cli_appaterno = models.CharField(db_column='CLI_APPATERNO', max_length=45)  # Field name made lowercase.
    cli_apmaterno = models.CharField(db_column='CLI_APMATERNO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cli_direcion = models.CharField(db_column='CLI_DIRECION', max_length=90, blank=True, null=True)  # Field name made lowercase.
    cli_celular = models.CharField(db_column='CLI_CELULAR', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cli_email = models.CharField(db_column='CLI_EMAIL', max_length=70, blank=True, null=True)  # Field name made lowercase.
    cli_nac = models.DateField(db_column='CLI_NAC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTE'

    def __str__(self):
        return self.cli_dni


class Estado(models.Model):
    est_id = models.IntegerField(db_column='EST_ID', primary_key=True)  # Field name made lowercase.
    est_nombre = models.CharField(db_column='EST_NOMBRE', max_length=70)  # Field name made lowercase.
    est_desc = models.CharField(db_column='EST_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADO'


class Mensaje(models.Model):
    men_id = models.AutoField(db_column='MEN_ID', primary_key=True)  # Field name made lowercase.
    men_nombre = models.CharField(db_column='MEN_NOMBRE', max_length=45)  # Field name made lowercase.
    men_contenido = models.CharField(db_column='MEN_CONTENIDO', max_length=400)  # Field name made lowercase.
    men_fechae = models.DateField(db_column='MEN_FECHAE')  # Field name made lowercase.
    tipo_tipo = models.ForeignKey('Tipo', db_column='TIPO_TIPO_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MENSAJE'


class Pago(models.Model):
    pago_id = models.IntegerField(db_column='PAGO_ID', primary_key=True)  # Field name made lowercase.
    pago_cuentadm = models.CharField(db_column='PAGO_CUENTADM', max_length=9)  # Field name made lowercase.
    pago_monto = models.DecimalField(db_column='PAGO_MONTO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    pago_fecha = models.DateTimeField(db_column='PAGO_FECHA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAGO'


class Reserva(models.Model):
    res_id = models.AutoField(db_column='RES_ID', primary_key=True)  # Field name made lowercase.
    res_fecha = models.DateTimeField(db_column='RES_FECHA')  # Field name made lowercase.
    res_cuentadm = models.CharField(db_column='RES_CUENTADM', max_length=9)   # Field name made lowercase.
    res_detalles = models.CharField(db_column='RES_DETALLES', max_length=300, blank=True, null=True)  # Field name made lowercase.
    cliente_cli = models.ForeignKey(Cliente, db_column='CLIENTE_CLI_ID')  # Field name made lowercase.
    mensaje_men = models.ForeignKey(Mensaje, db_column='MENSAJE_MEN_ID')  # Field name made lowercase.
    tarifa_tar = models.ForeignKey('Tarifa', db_column='TARIFA_TAR_ID')  # Field name made lowercase.
    pago_pago = models.ForeignKey(Pago, db_column='PAGO_PAGO_ID')  # Field name made lowercase.
    estado_est = models.ForeignKey(Estado, db_column='ESTADO_EST_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVA'


class Rol(models.Model):
    rol_id = models.IntegerField(db_column='ROL_ID', primary_key=True)  # Field name made lowercase.
    rol_nombre = models.CharField(db_column='ROL_NOMBRE', max_length=70)  # Field name made lowercase.
    rol_desc = models.CharField(db_column='ROL_DESC', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROL'


class Tarifa(models.Model):
    tar_id = models.IntegerField(db_column='TAR_ID', primary_key=True)  # Field name made lowercase.
    tar_nombre = models.CharField(db_column='TAR_NOMBRE', max_length=70)  # Field name made lowercase.
    tar_desc = models.CharField(db_column='TAR_DESC', max_length=200)  # Field name made lowercase.
    tar_costo = models.DecimalField(db_column='TAR_COSTO', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TARIFA'

    def __unicode__(self):
        return self.tar_nombre


class Tipo(models.Model):
    tipo_id = models.IntegerField(db_column='TIPO_ID', primary_key=True)  # Field name made lowercase.
    tipo_nombre = models.CharField(db_column='TIPO_NOMBRE', max_length=80)  # Field name made lowercase.
    tipo_des = models.CharField(db_column='TIPO_DES', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO'

#    dni = models.CharField(max_length=7, blank=True, null=True)
#    rol = models.ForeignKey(Rol, db_column='rol', blank=True, null=True)

