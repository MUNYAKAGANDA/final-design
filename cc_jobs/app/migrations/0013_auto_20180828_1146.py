# Generated by Django 2.0.4 on 2018-08-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180824_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='video',
            field=models.FileField(upload_to='videos/tigo'),
        ),
    ]
