# Generated by Django 4.2.5 on 2023-09-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_shifts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shifts',
            name='date',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='shifts',
            name='employee',
            field=models.ManyToManyField(to='employee.employee', verbose_name='Especilista'),
        ),
    ]
