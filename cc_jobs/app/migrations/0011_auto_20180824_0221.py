# Generated by Django 2.0.4 on 2018-08-24 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180824_0154'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Sponsorship',
        ),
    ]
