# Generated by Django 2.0.5 on 2018-05-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('En prestamo', 'En prestamo'), ('En reparacion', 'En reparacion'), ('Perdido', 'Perdido')], default='Disponible', max_length=15)),
                ('solicitudes', models.IntegerField(default=0)),
                ('imagen', models.ImageField(default='img/none.png', upload_to='img')),
            ],
        ),
    ]
