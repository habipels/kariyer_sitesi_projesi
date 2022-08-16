# Generated by Django 3.2.9 on 2022-03-04 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0019_company_profile'),
        ('offer', '0005_expert_expert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='offer_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.company_profile', verbose_name='Teklifi Yapan Kullanıcı'),
        ),
        migrations.AlterField(
            model_name='expert_expert',
            name='offer_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.user_profil', verbose_name='Teklifi Yapan Kullanıcı'),
        ),
    ]
