# Generated by Django 2.0.5 on 2019-11-17 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0008_auto_20191105_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('slug',)},
        ),
    ]
