# Generated by Django 3.2.9 on 2021-12-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211218_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='media/userprofile/default.jpg', max_length=254, upload_to='userprofile/', verbose_name='Image'),
        ),
    ]
