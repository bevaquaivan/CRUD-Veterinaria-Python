# Generated by Django 4.2 on 2023-05-04 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0003_alter_tipomascota_options_alter_mascota_propietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_consulta', models.DateField(verbose_name='Fecha de consulta')),
                ('observaciones', models.CharField(max_length=400, verbose_name='Observaciones Realizadas')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.mascota', verbose_name='Mascota')),
            ],
        ),
    ]