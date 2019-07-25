# Generated by Django 2.0.9 on 2019-07-17 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Organization Name',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
