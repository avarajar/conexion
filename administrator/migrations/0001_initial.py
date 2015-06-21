# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Co_Creadore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=144)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes_co_creadores', blank=True)),
                ('perfil', models.TextField(default=b'', help_text=b'Descripcion del Co_Creador')),
                ('twitter', models.URLField()),
                ('linkedin', models.URLField()),
                ('facebook', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Dinamica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('tipo_usuario', models.CharField(max_length=100, verbose_name=b'Seleccione tipo de usuario', choices=[(b'1', b'Global'), (b'2', b'Free'), (b'3', b'Premium')])),
                ('tipo_dinamica', models.CharField(max_length=100, verbose_name=b'Seleccione tipo de dinamica', choices=[(b'1', b'Individual'), (b'2', b'Grupal')])),
                ('limite_participantes', models.IntegerField()),
                ('tiempo_desarrollo', models.TimeField()),
                ('descripcion', models.TextField(default=b'', help_text=b'Descripcion de la dinamica')),
                ('objetivo_general', models.CharField(max_length=250, null=True, blank=True)),
                ('objetivo_especifico_uno', models.CharField(max_length=250, null=True, blank=True)),
                ('objetivo_especifico_dos', models.CharField(max_length=250, null=True, blank=True)),
                ('objetivo_especifico_tres', models.CharField(max_length=250, null=True, blank=True)),
                ('imagen_uno', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_dos', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_tres', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_cuatro', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_cinco', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_seis', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_siete', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_ocho', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_nueve', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('imagen_diez', models.ImageField(null=True, upload_to=b'imagenes_dinamicas/', blank=True)),
                ('slug', models.SlugField(default=b'', max_length=250, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes_retos/', blank=True)),
                ('participantes', models.IntegerField()),
                ('duracion', models.TimeField()),
                ('descripcion', models.TextField(default=b'', help_text=b'Descripcion del Reto ')),
                ('objetivo_general', models.CharField(max_length=250, null=True, blank=True)),
                ('objetivo_especifico_uno', models.CharField(max_length=250, null=True, blank=True)),
                ('objetivo_especifico_dos', models.CharField(max_length=250, null=True, blank=True)),
                ('objetivo_especifico_tres', models.CharField(max_length=250, null=True, blank=True)),
                ('recompensa', models.TextField(default=b'', help_text=b'Recompensa del Reto')),
                ('evidencias', models.DateTimeField()),
                ('aprendizajes', models.DateTimeField()),
                ('soluciones', models.DateTimeField()),
                ('resultados', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=50)),
                ('slug', models.SlugField(default=b'', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='dinamica',
            name='tags',
            field=models.ForeignKey(to='administrator.Tag'),
        ),
    ]
