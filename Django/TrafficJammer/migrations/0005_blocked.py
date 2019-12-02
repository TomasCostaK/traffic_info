# Generated by Django 2.2.6 on 2019-12-02 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficJammer', '0004_auto_20191202_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrafficJammer.Section')),
            ],
        ),
    ]
