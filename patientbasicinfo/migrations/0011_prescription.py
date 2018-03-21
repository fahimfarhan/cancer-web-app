# Generated by Django 2.0.3 on 2018-03-21 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientbasicinfo', '0010_auto_20180321_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('details', models.CharField(blank=True, max_length=1000)),
                ('identity_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patientbasicinfo.Identity')),
            ],
        ),
    ]
