# Generated by Django 5.2 on 2025-05-06 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_studentprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='name',
        ),
    ]
