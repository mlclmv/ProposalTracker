# Generated by Django 2.0.9 on 2019-07-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYPSamhita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposaldoc',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]