# Generated by Django 3.2.9 on 2022-02-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0016_auto_20220223_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profil',
            name='background',
            field=models.FileField(blank=True, null=True, upload_to='back/', verbose_name='Arkaplan Görseli'),
        ),
        migrations.AlterField(
            model_name='user_profil',
            name='profil_img',
            field=models.FileField(blank=True, null=True, upload_to='profil/', verbose_name='Profil Görseli'),
        ),
    ]
