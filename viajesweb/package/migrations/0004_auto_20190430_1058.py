# Generated by Django 2.1.7 on 2019-04-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_auto_20190429_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internacionale',
            name='descripcion',
            field=models.CharField(max_length=98),
        ),
        migrations.AlterField(
            model_name='nacionale',
            name='descripcion',
            field=models.CharField(max_length=98),
        ),
    ]