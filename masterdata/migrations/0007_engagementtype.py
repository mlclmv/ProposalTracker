# Generated by Django 2.0.9 on 2019-07-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0006_auto_20190719_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngagementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
