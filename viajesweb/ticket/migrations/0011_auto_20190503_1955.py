# Generated by Django 2.1.7 on 2019-05-04 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_auto_20190503_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='asientos',
            field=models.IntegerField(),
        ),
    ]
