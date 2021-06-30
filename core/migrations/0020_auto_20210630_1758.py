# Generated by Django 3.2.4 on 2021-06-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210630_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='rut',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='datetime',
            field=models.DateField(blank=True, null=True),
        ),
    ]
