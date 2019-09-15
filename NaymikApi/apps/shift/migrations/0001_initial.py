# Generated by Django 2.2.5 on 2019-09-14 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0002_auto_20190914_1716'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniform', models.ImageField(upload_to='')),
                ('workers_number', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('description', models.TextField()),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shift_employer', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shift_custom_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'shift',
                'verbose_name_plural': 'shift',
                'db_table': 'shift',
            },
        ),
        migrations.CreateModel(
            name='ShiftSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_skills_base_skill', to='skills.BaseSkill')),
                ('shift_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_skills_shift_role', to='shift.Shift')),
            ],
            options={
                'verbose_name': 'shift_skill',
                'verbose_name_plural': 'shift_skill',
                'db_table': 'shift_skill',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_shift', to='shift.Shift')),
            ],
        ),
    ]