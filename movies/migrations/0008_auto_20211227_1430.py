# Generated by Django 3.2.9 on 2021-12-27 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0007_auto_20211227_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielikedislike',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movieprofile', to='movies.movies'),
        ),
        migrations.AlterField(
            model_name='movielikedislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]