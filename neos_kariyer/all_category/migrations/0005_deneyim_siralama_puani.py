# Generated by Django 3.2.9 on 2022-03-10 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_category', '0004_ucretlendirme'),
    ]

    operations = [
        migrations.AddField(
            model_name='deneyim',
            name='siralama_puani',
            field=models.IntegerField(null=True),
        ),
    ]