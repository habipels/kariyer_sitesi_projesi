# Generated by Django 3.2.9 on 2022-02-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_status',
            name='durum',
            field=models.BooleanField(null=True),
        ),
    ]
