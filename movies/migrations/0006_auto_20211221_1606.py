# Generated by Django 3.2.9 on 2021-12-21 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20211221_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='dislike_count',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='like_count',
        ),
    ]