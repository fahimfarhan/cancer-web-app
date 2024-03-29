# Generated by Django 2.0.3 on 2018-03-21 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chemotherapy', '0002_auto_20180320_1221'),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActCycle',
            fields=[
                ('cycle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tables.Cycle')),
                ('act_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemotherapy.ChemoTherapy')),
            ],
            bases=('tables.cycle',),
        ),
        migrations.CreateModel(
            name='ConcurrentCycle',
            fields=[
                ('cycle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tables.Cycle')),
                ('concurr_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemotherapy.ChemoTherapy')),
            ],
            bases=('tables.cycle',),
        ),
        migrations.CreateModel(
            name='PalliativeCycle',
            fields=[
                ('cycle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tables.Cycle')),
                ('palliative_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemotherapy.ChemoTherapy')),
            ],
            bases=('tables.cycle',),
        ),
    ]
