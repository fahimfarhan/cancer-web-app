# Generated by Django 2.0.3 on 2018-03-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_brachychart_cobaltchart_linacchart_radiotherapychart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiotherapychart',
            name='fieldsize',
            field=models.FloatField(blank=True),
        ),
    ]