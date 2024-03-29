# Generated by Django 3.2.9 on 2021-12-06 18:57

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, validators=[users.validators.DomainUnicodeusernameValidator], verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('firstname', models.CharField(max_length=40, validators=[users.validators.DomainUnicodenameValidator], verbose_name='firstname')),
                ('lastname', models.CharField(max_length=30, validators=[users.validators.DomainUnicodenameValidator], verbose_name='lastname')),
                ('mobile', models.CharField(max_length=10, validators=[users.validators.DomainUnicodemobileValidator], verbose_name='mobile')),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
