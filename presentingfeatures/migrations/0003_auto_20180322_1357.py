# Generated by Django 2.0.3 on 2018-03-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentingfeatures', '0002_investigation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='advice',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='status',
            name='details',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
