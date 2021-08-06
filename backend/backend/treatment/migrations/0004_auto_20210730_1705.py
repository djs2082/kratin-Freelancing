# Generated by Django 3.2.5 on 2021-07-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0003_parametermodel_patientparametermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientparametermodel',
            name='parameter',
        ),
        migrations.RemoveField(
            model_name='patientparametermodel',
            name='value',
        ),
        migrations.AddField(
            model_name='patientparametermodel',
            name='heartbeat',
            field=models.IntegerField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='patientparametermodel',
            name='spo2',
            field=models.IntegerField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='patientparametermodel',
            name='temperature',
            field=models.FloatField(default=0.0),
        ),
    ]