# Generated by Django 3.2.15 on 2023-04-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0005_auto_20230315_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftregistration',
            name='aircraft_mfr_model_code',
            field=models.CharField(blank=True, db_index=True, max_length=7, null=True),
        ),
    ]