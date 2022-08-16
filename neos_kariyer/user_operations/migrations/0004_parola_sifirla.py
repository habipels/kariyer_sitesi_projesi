# Generated by Django 3.2.9 on 2022-03-22 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operations', '0003_alter_user_status_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='parola_sifirla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifirla', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Durumu')),
            ],
        ),
    ]
