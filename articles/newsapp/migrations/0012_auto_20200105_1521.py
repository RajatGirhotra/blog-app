# Generated by Django 3.0.2 on 2020-01-05 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0011_auto_20200105_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Artciles'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': "Customer's"},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tags'},
        ),
    ]
