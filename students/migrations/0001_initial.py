# Generated by Django 3.2.20 on 2023-07-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('field_of_study', models.CharField(max_length=50)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
