# Generated by Django 3.2.9 on 2022-03-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad_offer_user',
            name='offer_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
