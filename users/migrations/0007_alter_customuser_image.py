# Generated by Django 3.2.9 on 2021-12-22 07:18

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='static/media/default.jpg', max_length=254, upload_to=users.models.nameFile, verbose_name='Image'),
        ),
    ]