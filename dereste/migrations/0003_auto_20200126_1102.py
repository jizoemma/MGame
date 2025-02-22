# Generated by Django 3.0.2 on 2020-01-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dereste', '0002_auto_20200112_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='grade',
            field=models.CharField(choices=[('DEBUT', 'DEBUT'), ('REGULAR', 'REGULAR'), ('PRO', 'PRO'), ('MASTER', 'MASTER'), ('MASTER_PLUS', 'MASTER_PLUS'), ('Legend_MASTER_PLUS', 'Legend_MASTER_PLUS'), ('FORTE', 'FORTE'), ('PIANO', 'PIANO'), ('LIGHT', 'LIGHT'), ('TRICK', 'TRICK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='songs',
            name='type',
            field=models.CharField(choices=[('Cute', 'Cute'), ('Cool', 'Cool'), ('Passion', 'Passion'), ('All', 'All')], max_length=50),
        ),
    ]
