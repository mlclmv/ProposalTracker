# Generated by Django 2.0.9 on 2019-07-22 11:04

from django.db import migrations, models
import django.db.models.deletion
import organization.models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0007_engagementtype'),
        ('organization', '0005_profile_org_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cause_area',
            field=models.ManyToManyField(blank=True, help_text='CSR Priorities', to='masterdata.CauseArea'),
        ),
        migrations.AddField(
            model_name='profile',
            name='main_partner',
            field=models.ForeignKey(blank=True, help_text='Exclusive partner if any ', null=True, on_delete=django.db.models.deletion.PROTECT, to='organization.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='mkt_position',
            field=models.TextField(blank=True, help_text='Market positioning', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='partners',
            field=models.ManyToManyField(blank=True, help_text='Other Partners', related_name='_profile_partners_+', to='organization.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='risks',
            field=models.TextField(blank=True, help_text='Risks associated (Reputation/ Default etc.)Risks associated (Reputation/ Default etc.)', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='statements',
            field=models.FileField(blank=True, help_text='Financial Statements - Last 3 years', null=True, upload_to=organization.models.get_upload_to),
        ),
        migrations.AddField(
            model_name='profile',
            name='vision',
            field=models.TextField(blank=True, help_text='Vision Statement', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='industry',
            field=models.ManyToManyField(blank=True, help_text='Area of work', related_name='org_details', to='masterdata.Industry'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location_city',
            field=models.ManyToManyField(blank=True, help_text='Cities with geographical presence', related_name='org_city', to='cities_light.City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location_state',
            field=models.ManyToManyField(blank=True, help_text='States with geographical presence', related_name='org_state', to='cities_light.Region'),
        ),
    ]
