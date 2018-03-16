# Generated by Django 2.0.3 on 2018-03-16 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobileNo', models.IntegerField(db_index=True, default=0)),
                ('dateOfAdmission', models.DateField(default=django.utils.timezone.now)),
                ('unit', models.CharField(blank=True, max_length=5)),
                ('religion', models.CharField(blank=True, max_length=5)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('dateOfBirth', models.DateField(blank=True)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('referredBy', models.CharField(blank=True, max_length=50)),
                ('regNo', models.CharField(blank=True, max_length=6)),
                ('image', models.ImageField(blank=True, upload_to='uploads/profile_pic/%Y/%m/%d/%H/%M/%S/')),
            ],
        ),
    ]
