# Generated by Django 3.2.6 on 2021-12-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feets', '0016_auto_20211226_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feet',
            name='Function',
        ),
        migrations.RemoveField(
            model_name='feet',
            name='Traffic',
        ),
        migrations.AddField(
            model_name='feet',
            name='function',
            field=models.ManyToManyField(blank=True, related_name='feets', to='feets.Function'),
        ),
        migrations.AddField(
            model_name='feet',
            name='traffic',
            field=models.ManyToManyField(blank=True, related_name='feets', to='feets.Traffic'),
        ),
        migrations.AddField(
            model_name='feet',
            name='waterproof',
            field=models.BooleanField(default=False),
        ),
    ]
