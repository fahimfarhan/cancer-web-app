# Generated by Django 2.0.3 on 2018-03-16 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientbasicinfo', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stage',
            field=models.IntegerField(default=1),
        ),
    ]
