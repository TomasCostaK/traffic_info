# Generated by Django 2.2.6 on 2019-12-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficJammer', '0006_auto_20191202_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocked',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
