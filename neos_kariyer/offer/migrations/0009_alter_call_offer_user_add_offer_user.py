# Generated by Django 3.2.9 on 2022-03-22 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0027_fav_adds_fav_user'),
        ('offer', '0008_call_offer_user_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_offer_user_add',
            name='offer_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.user_profil', verbose_name='İlan Teklifi Yapan '),
        ),
    ]
