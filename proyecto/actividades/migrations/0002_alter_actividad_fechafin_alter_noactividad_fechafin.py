# Generated by Django 4.2.6 on 2023-10-25 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fechafin',
            field=models.DateField(max_length=25),
        ),
        migrations.AlterField(
            model_name='noactividad',
            name='fechafin',
            field=models.DateField(max_length=25),
        ),
    ]