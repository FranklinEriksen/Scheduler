# Generated by Django 2.2.6 on 2019-12-05 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_empinfo_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='currentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentUsename', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
