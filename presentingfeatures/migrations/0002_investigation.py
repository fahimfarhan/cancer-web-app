# Generated by Django 2.0.3 on 2018-03-19 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientbasicinfo', '0007_bangla_dose_medicine_timetable'),
        ('presentingfeatures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='uploads/pf_file/%Y/%m/%d/%H/%M/%S/')),
                ('fnum', models.IntegerField(default=0)),
                ('name', models.CharField(default='name unavailable', max_length=100)),
                ('identity_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientbasicinfo.Identity')),
            ],
        ),
    ]
