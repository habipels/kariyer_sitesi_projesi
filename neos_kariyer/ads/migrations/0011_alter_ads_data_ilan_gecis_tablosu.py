# Generated by Django 3.2.9 on 2022-03-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_alter_ads_data_ilan_gecis_tablosu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads_data',
            name='ilan_gecis_tablosu',
            field=models.DateTimeField(null=True, verbose_name='İlan Kalma Tarihi'),
        ),
    ]
