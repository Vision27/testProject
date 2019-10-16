# Generated by Django 2.2.6 on 2019-10-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('million', '0002_auto_20191016_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concert',
            name='Concert_ft',
        ),
        migrations.RemoveField(
            model_name='singer',
            name='singer_prize',
        ),
        migrations.AddField(
            model_name='singer',
            name='singer_price',
            field=models.CharField(default='', max_length=20, verbose_name='Price of singer'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='Concert_date',
            field=models.CharField(default='', max_length=20, verbose_name='Concert date'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='Concert_name',
            field=models.CharField(default='', max_length=20, verbose_name='Concert name'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='Concert_place',
            field=models.CharField(default='', max_length=20, verbose_name='Concert place'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='Concert_price',
            field=models.CharField(default='', max_length=20, verbose_name='Concert price'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='Concert_time',
            field=models.CharField(default='', max_length=20, verbose_name='Concert time'),
        ),
        migrations.AlterField(
            model_name='singer',
            name='singer_age',
            field=models.IntegerField(default='', verbose_name='Age of singer'),
        ),
        migrations.AlterField(
            model_name='singer',
            name='singer_reputation',
            field=models.CharField(default='', max_length=20, verbose_name='Reputation of singer'),
        ),
        migrations.AlterField(
            model_name='singer',
            name='singer_sex',
            field=models.CharField(default='', max_length=20, verbose_name='Sex of singer'),
        ),
        migrations.AlterField(
            model_name='singer',
            name='singer_style',
            field=models.CharField(default='', max_length=20, verbose_name='Style of singer'),
        ),
    ]