# Generated by Django 2.0.9 on 2019-07-23 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0008_auto_20190723_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('stage', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stage_fk', to='masterdata.ProposalStage')),
                ('workflow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='workflow_fk', to='masterdata.Workflow')),
            ],
        ),
    ]