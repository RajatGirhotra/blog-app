# Generated by Django 3.0.2 on 2020-01-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_auto_20200105_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
