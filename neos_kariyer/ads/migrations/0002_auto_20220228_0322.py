# Generated by Django 3.2.9 on 2022-02-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads_data',
            name='chip_amunt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ads_data',
            name='offer_much',
            field=models.IntegerField(null=True),
        ),
    ]
