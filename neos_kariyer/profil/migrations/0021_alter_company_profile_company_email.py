# Generated by Django 3.2.9 on 2022-03-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0020_profil_acma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_profile',
            name='company_email',
            field=models.EmailField(max_length=22, null=True, verbose_name='E-Posta'),
        ),
    ]
