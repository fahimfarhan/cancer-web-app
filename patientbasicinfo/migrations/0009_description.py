# Generated by Django 2.0.3 on 2018-03-21 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientbasicinfo', '0008_treatmentplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=1000)),
                ('identity_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patientbasicinfo.Identity')),
            ],
        ),
    ]
