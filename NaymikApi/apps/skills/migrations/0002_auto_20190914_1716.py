# Generated by Django 2.2.5 on 2019-09-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseskill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
