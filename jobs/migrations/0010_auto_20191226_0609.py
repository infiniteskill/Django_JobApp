# Generated by Django 3.0 on 2019-12-26 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_remove_job_domain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='approach',
            new_name='contact',
        ),
    ]
