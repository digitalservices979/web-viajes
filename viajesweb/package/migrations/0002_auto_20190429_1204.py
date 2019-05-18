# Generated by Django 2.1.7 on 2019-04-29 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internacionale',
            options={'ordering': ['-created'], 'verbose_name': 'Internacional', 'verbose_name_plural': 'Internacionales'},
        ),
        migrations.AlterModelOptions(
            name='nacionale',
            options={'ordering': ['-created'], 'verbose_name': 'Nacional', 'verbose_name_plural': 'Nacionales'},
        ),
        migrations.AddField(
            model_name='internacionale',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nacionale',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
    ]
