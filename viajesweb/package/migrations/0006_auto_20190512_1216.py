# Generated by Django 2.1.7 on 2019-05-12 17:16

from django.db import migrations, models
import package.models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_auto_20190430_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internacionale',
            name='imagen',
            field=models.ImageField(upload_to=package.models.custom_upload_to),
        ),
    ]