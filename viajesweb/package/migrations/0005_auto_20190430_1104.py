# Generated by Django 2.1.7 on 2019-04-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_auto_20190430_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internacionale',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='nacionale',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
