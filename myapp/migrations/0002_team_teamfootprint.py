# Generated by Django 3.0.6 on 2021-01-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='teamfootprint',
            field=models.IntegerField(default=0),
        ),
    ]
