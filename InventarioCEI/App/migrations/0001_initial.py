# Generated by Django 2.0.5 on 2018-06-29 20:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userSystem', '0002_auto_20180525_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aforo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prestables',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('En prestamo', 'En prestamo'), ('En reparacion', 'En reparacion'), ('Perdido', 'Perdido')], default='Disponible', max_length=15)),
                ('imagen', models.ImageField(default='img/none.png', upload_to='img')),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('numsolic', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('tiempo_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('tiempo_final', models.DateTimeField(default=django.utils.timezone.now)),
                ('tiempo_solicitud', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado_sol', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aceptada', 'Aceptada'), ('Rechazada', 'Rechazada')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('solicitud_aceptada', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='App.Solicitudes')),
                ('estado_sol', models.CharField(choices=[('Vigente', 'Vigente'), ('Caducada', 'Caducada'), ('Perdida', 'Perdida')], max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='solicitudes',
            name='persona',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userSystem.Usuarios'),
        ),
        migrations.AddField(
            model_name='solicitudes',
            name='prestable',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App.Prestables'),
        ),
        migrations.AddField(
            model_name='aforo',
            name='espacio',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='App.Prestables'),
        ),
    ]
