# Generated by Django 2.2.5 on 2019-09-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerrole',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
