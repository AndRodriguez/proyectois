# Generated by Django 4.0.4 on 2022-08-22 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0005_alter_categoria_fecharegistro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 6446)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 6446)),
        ),
        migrations.AlterField(
            model_name='detalledocumentocompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 12433)),
        ),
        migrations.AlterField(
            model_name='detalledocumentoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 11441)),
        ),
        migrations.AlterField(
            model_name='detallenotaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 10438)),
        ),
        migrations.AlterField(
            model_name='detalleordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 9440)),
        ),
        migrations.AlterField(
            model_name='detallepedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 8443)),
        ),
        migrations.AlterField(
            model_name='documentocompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 12433)),
        ),
        migrations.AlterField(
            model_name='documentoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 11441)),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 6446)),
        ),
        migrations.AlterField(
            model_name='notaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 10438)),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 9440)),
        ),
        migrations.AlterField(
            model_name='pedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 7412)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaCargaImagen',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 7412)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreImagen',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='urlImagen',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 8443)),
        ),
        migrations.AlterField(
            model_name='tipocliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 5460)),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 49, 30, 5460)),
        ),
    ]
