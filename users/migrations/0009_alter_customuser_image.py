# Generated by Django 3.2.9 on 2021-12-23 09:56

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20211223_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to=users.models.nameFile, verbose_name='image'),
        ),
    ]