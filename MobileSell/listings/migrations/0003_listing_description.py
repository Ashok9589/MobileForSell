# Generated by Django 3.0.4 on 2020-03-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_modelname'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
