# Generated by Django 2.0.9 on 2019-08-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYPSamhita', '0004_auto_20190802_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposaldoc',
            name='doc',
            field=models.FileField(blank=True, help_text='Upload file', null=True, upload_to='proposal_docs/%Y-%m/'),
        ),
    ]