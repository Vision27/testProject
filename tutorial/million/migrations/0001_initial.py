# Generated by Django 2.2.6 on 2019-10-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex_name', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
