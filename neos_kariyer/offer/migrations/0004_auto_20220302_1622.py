# Generated by Django 3.2.9 on 2022-03-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_expert'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad_offer_user',
            name='veto_status',
            field=models.BooleanField(null=True, verbose_name='Red Durumu'),
        ),
        migrations.AddField(
            model_name='expert',
            name='veto_status',
            field=models.BooleanField(null=True, verbose_name='Red Durumu'),
        ),
    ]
