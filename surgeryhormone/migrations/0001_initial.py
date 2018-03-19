# Generated by Django 2.0.3 on 2018-03-19 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patientbasicinfo', '0008_treatmentplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hormone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=200)),
                ('tp_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patientbasicinfo.TreatmentPlan')),
            ],
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=200)),
                ('tp_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patientbasicinfo.TreatmentPlan')),
            ],
        ),
    ]
