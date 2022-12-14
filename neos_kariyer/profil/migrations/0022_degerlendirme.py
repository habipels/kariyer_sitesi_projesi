# Generated by Django 3.2.9 on 2022-03-10 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profil', '0021_alter_company_profile_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='degerlendirme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puan', models.IntegerField()),
                ('profil', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.user_profil', verbose_name='Oy Alan')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Oy Veren')),
            ],
        ),
    ]
