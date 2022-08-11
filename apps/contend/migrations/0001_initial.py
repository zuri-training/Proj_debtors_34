# Generated by Django 4.0.6 on 2022-08-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='default', max_length=100000000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(default='default', max_length=1000)),
                ('room', models.CharField(default='default', max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=4)),
            ],
        ),
    ]
