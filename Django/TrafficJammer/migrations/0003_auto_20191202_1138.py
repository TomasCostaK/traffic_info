# Generated by Django 2.2.6 on 2019-12-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficJammer', '0002_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AlterField(
            model_name='car',
            name='license_plate',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]