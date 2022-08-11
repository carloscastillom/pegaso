# Generated by Django 4.1 on 2022-08-07 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('priority', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('time_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
