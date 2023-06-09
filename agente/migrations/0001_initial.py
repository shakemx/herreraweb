# Generated by Django 4.2.1 on 2023-06-29 16:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('nombre', models.CharField(max_length=200, verbose_name='Agente')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Foto Agente')),
                ('portada', models.ImageField(upload_to='', verbose_name='Portada Presentación')),
                ('bio', models.TextField(default='Profesional de Seguros, experto en prevención de riesgos y cuidado patrimonial', verbose_name='Biografía')),
                ('perfil', models.CharField(default='Agente de Seguros', verbose_name='Puesto')),
                ('url_ubicacion', models.URLField(verbose_name='URL Google Maps')),
                ('direccion', models.CharField(max_length=200, verbose_name='Lugar de Trabajo')),
                ('horario', models.CharField(default='Lun - Vie 9 a 18 hrs', verbose_name='Horario Laboral')),
                ('telefono', models.CharField(blank=True, max_length=12, null=True, verbose_name='Teléfono')),
                ('movil', models.CharField(max_length=12, verbose_name='Celular')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Youtube')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
            ],
            options={
                'verbose_name': 'Agente',
                'verbose_name_plural': 'Agentes',
            },
        ),
    ]
