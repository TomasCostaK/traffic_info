# Generated by Django 3.0 on 2019-12-18 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_cars', models.IntegerField(default=0)),
                ('actual_direction', models.BooleanField()),
                ('n_accident', models.IntegerField(default=0)),
                ('beginning_coords_x', models.IntegerField()),
                ('ending_coords_x', models.IntegerField()),
                ('beginning_coords_y', models.IntegerField()),
                ('ending_coords_y', models.IntegerField()),
                ('visibility', models.IntegerField(default=100)),
                ('roadblock', models.BooleanField(default=False)),
                ('police', models.BooleanField(default=False)),
                ('connect_to', models.ManyToManyField(blank=True, related_name='_section_connect_to_+', to='TrafficJammer.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('begin_coord_x', models.IntegerField()),
                ('begin_coord_y', models.IntegerField()),
                ('ending_coord_x', models.IntegerField()),
                ('ending_coord_y', models.IntegerField()),
                ('city', models.CharField(max_length=80)),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrafficJammer.Section')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrafficJammer.Street'),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('license_plate', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrafficJammer.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Blocked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrafficJammer.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coord_x', models.IntegerField()),
                ('coord_y', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrafficJammer.Section')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('street', 'beginning_coords_x', 'beginning_coords_y', 'actual_direction')},
        ),
    ]
