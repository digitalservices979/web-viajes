# Generated by Django 2.1.7 on 2019-05-02 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20190502_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasajero',
            name='fecha',
        ),
    ]
