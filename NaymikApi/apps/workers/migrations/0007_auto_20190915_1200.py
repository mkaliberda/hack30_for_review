# Generated by Django 2.2.5 on 2019-09-15 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0006_workerrole_roles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workerrole',
            old_name='roles',
            new_name='skills_roles',
        ),
    ]
