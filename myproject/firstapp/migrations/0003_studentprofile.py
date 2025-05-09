# Generated by Django 5.2 on 2025-05-06 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_student_teacher_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('mobile', models.IntegerField()),
                ('bio', models.TextField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firstapp.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
