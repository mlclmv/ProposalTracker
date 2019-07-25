# Generated by Django 2.0.9 on 2019-07-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0011_auto_20190723_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnershipLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
