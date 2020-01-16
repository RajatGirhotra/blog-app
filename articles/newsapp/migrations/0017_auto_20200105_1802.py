# Generated by Django 3.0.2 on 2020-01-05 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0016_auto_20200105_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.AddField(
            model_name='article',
            name='auto_increment_id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]