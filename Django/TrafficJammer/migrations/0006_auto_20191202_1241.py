# Generated by Django 2.2.6 on 2019-12-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficJammer', '0005_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocked',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
    ]