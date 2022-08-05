# Generated by Django 4.0.6 on 2022-08-04 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], max_length=50)),
            ],
        ),
    ]
