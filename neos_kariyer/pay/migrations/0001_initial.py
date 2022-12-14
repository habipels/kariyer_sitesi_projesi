# Generated by Django 3.2.9 on 2022-03-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ads_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paket_basligi', models.CharField(max_length=50, verbose_name='İlan')),
                ('kisa_ilan_aciklamasi', models.CharField(max_length=250, verbose_name='Kısa İlan Açıklaması')),
                ('ilan_olusturma_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('İlan_gorseli', models.FileField(blank=True, null=True, upload_to='paket/', verbose_name='ilana Fotoğraf Ekleyin')),
                ('ilana_alinacak_ucret', models.IntegerField(null=True)),
                ('teklife_verilecek_ucret', models.IntegerField(null=True)),
            ],
        ),
    ]
