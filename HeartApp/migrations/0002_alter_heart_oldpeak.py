# Generated by Django 3.2.3 on 2021-07-21 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heart',
            name='oldpeak',
            field=models.FloatField(),
        ),
    ]