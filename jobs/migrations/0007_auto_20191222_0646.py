# Generated by Django 3.0 on 2019-12-22 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20191222_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='postdate',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]
