# Generated by Django 2.2.6 on 2019-11-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empinfo',
            name='fri',
            field=models.CharField(default='000000000000000000000000', max_length=24),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='mon',
            field=models.CharField(default='000000000000000000000000', max_length=24),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='sat',
            field=models.CharField(default='000000000000000000000000', max_length=24),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='sun',
            field=models.CharField(default='000000000000000000000000', max_length=24),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='thurs',
            field=models.CharField(default='000000000000000000000000', max_length=24),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='tues',
            field=models.CharField(default='000000000000000000000000', max_length=24),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='wed',
            field=models.CharField(default='000000000000000000000000', max_length=24),
        ),
    ]
