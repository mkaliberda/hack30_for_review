# Generated by Django 2.2.5 on 2019-09-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0004_auto_20190914_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='faculty',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='experience',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
    ]
