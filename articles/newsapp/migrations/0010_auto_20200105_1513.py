# Generated by Django 3.0.2 on 2020-01-05 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0009_auto_20200105_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newsapp.Customer'),
        ),
    ]
