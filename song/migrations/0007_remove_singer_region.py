# Generated by Django 2.0.5 on 2019-11-04 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0006_auto_20191104_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singer',
            name='region',
        ),
    ]
