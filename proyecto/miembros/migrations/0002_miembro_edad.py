# Generated by Django 4.2.6 on 2023-10-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='edad',
            field=models.CharField(default=0, max_length=10, verbose_name='Edad'),
        ),
    ]