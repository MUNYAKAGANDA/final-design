# Generated by Django 2.0.4 on 2018-08-28 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20180828_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='slug',
        ),
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
