# Generated by Django 2.2.5 on 2019-09-14 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_company_company', to='employers.Company')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_company_employer_role', to='employers.EmployerRole')),
            ],
            options={
                'verbose_name': 'employer_company',
                'verbose_name_plural': 'employer_company',
                'db_table': 'employer_company',
            },
        ),
    ]