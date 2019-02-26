# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(null=True)),
                ('autor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_devolucion', models.IntegerField(null=True)),
                ('libros_prestados', models.IntegerField(null=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.Libros')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.Socio'),
        ),
    ]
