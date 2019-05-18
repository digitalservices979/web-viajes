# Generated by Django 2.1.7 on 2019-05-02 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_remove_pasajero_asientos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasajero',
            name='asientos',
            field=models.SmallIntegerField(default=datetime.datetime(2019, 5, 2, 16, 41, 4, 154725, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pasajero',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2019, 5, 2, 16, 41, 23, 936197, tzinfo=utc)),
            preserve_default=False,
        ),
    ]