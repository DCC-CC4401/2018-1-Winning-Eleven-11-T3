# Generated by Django 2.0.5 on 2018-05-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]