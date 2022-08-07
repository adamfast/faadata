# Generated by Django 3.2.15 on 2022-08-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0003_auto_20210109_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftmanufacturercode',
            name='aircraft_type',
            field=models.CharField(choices=[('1', 'Glider'), ('2', 'Balloon'), ('3', 'Blimp/Dirigible'), ('4', 'Fixed wing single engine'), ('5', 'Fixed wing multi engine'), ('6', 'Rotorcraft'), ('7', 'Weight-shift-control'), ('8', 'Powered Parachute'), ('9', 'Gyroplane'), ('H', 'Powered Lift'), ('O', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='aircraftregistration',
            name='aircraft_type',
            field=models.CharField(blank=True, choices=[('1', 'Glider'), ('2', 'Balloon'), ('3', 'Blimp/Dirigible'), ('4', 'Fixed wing single engine'), ('5', 'Fixed wing multi engine'), ('6', 'Rotorcraft'), ('7', 'Weight-shift-control'), ('8', 'Powered Parachute'), ('9', 'Gyroplane'), ('H', 'Powered Lift'), ('O', 'Other')], default='', max_length=1),
        ),
    ]
