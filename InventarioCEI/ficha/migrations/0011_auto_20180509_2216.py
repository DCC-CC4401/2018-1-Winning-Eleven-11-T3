# Generated by Django 2.0.5 on 2018-05-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0010_auto_20180509_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestables',
            name='id',
            field=models.IntegerField(default=94523412, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='id',
            field=models.IntegerField(default=16964724, editable=False, primary_key=True, serialize=False),
        ),
    ]
