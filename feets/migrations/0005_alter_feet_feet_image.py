# Generated by Django 3.2.6 on 2021-09-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feets', '0004_auto_20210910_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feet',
            name='feet_image',
            field=models.ImageField(blank=True, upload_to='feets'),
        ),
    ]
