# Generated by Django 2.2.5 on 2019-09-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20190914_1716'),
        ('workers', '0005_auto_20190914_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerrole',
            name='roles',
            field=models.ManyToManyField(to='skills.BaseSkill'),
        ),
    ]