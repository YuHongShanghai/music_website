# Generated by Django 2.0.5 on 2019-11-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('region', models.CharField(choices=[(1, '中国大陆'), (2, '港台'), (3, '欧美'), (4, '其他'), (5, '未知')], default=5, max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]