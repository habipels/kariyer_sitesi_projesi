# Generated by Django 3.2.9 on 2022-03-22 04:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0027_fav_adds_fav_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profil',
            name='user_about',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
