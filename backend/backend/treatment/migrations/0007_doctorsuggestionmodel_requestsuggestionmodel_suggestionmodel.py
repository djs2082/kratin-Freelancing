# Generated by Django 3.2.5 on 2021-08-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('treatment', '0006_auto_20210804_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RequestSuggestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.requestsmodel')),
                ('suggestion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='treatment.suggestionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSuggestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.doctormodel')),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.suggestionmodel')),
            ],
        ),
    ]
