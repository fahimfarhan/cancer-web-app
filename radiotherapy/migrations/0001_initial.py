# Generated by Django 2.0.3 on 2018-03-20 04:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patientbasicinfo', '0008_treatmentplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadioTherapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, max_length=10)),
                ('intensity', models.CharField(blank=True, max_length=50)),
                ('dose', models.CharField(blank=True, max_length=50)),
                ('gray', models.FloatField(blank=True, default=0)),
                ('fractionFx', models.FloatField(blank=True, default=0)),
                ('startDate', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('endDate', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('details', models.CharField(blank=True, max_length=200)),
                ('tp_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientbasicinfo.TreatmentPlan')),
            ],
        ),
    ]