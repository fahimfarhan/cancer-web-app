# Generated by Django 2.0.3 on 2018-03-16 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientbasicinfo', '0003_comorbidity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseaseCode', models.CharField(max_length=50)),
                ('histopathology', models.CharField(max_length=50)),
                ('ihc', models.CharField(max_length=50)),
                ('er_pr', models.CharField(max_length=50)),
                ('stage', models.IntegerField(default=1, max_length=4)),
                ('tnm', models.CharField(max_length=50)),
                ('height', models.FloatField(max_length=5)),
                ('weight', models.FloatField(max_length=5)),
                ('bsa', models.FloatField(default=0, max_length=10)),
                ('ps', models.CharField(max_length=10)),
                ('bloodGroup', models.CharField(max_length=3)),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientbasicinfo.Identity')),
            ],
        ),
    ]
