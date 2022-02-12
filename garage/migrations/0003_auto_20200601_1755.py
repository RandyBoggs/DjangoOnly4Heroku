# Generated by Django 3.0.6 on 2020-06-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='point_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.PointType'),
        ),
    ]