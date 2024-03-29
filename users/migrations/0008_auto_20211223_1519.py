# Generated by Django 3.2.9 on 2021-12-23 09:49

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to=users.models.nameFile, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(max_length=30, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(max_length=10, verbose_name='mobile'),
        ),
    ]
