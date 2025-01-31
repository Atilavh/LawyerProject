# Generated by Django 4.1.13 on 2024-08-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('FullName', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('PhoneNumber', models.CharField(max_length=11, unique=True, verbose_name='شماره تماس')),
            ],
            options={
                'verbose_name': 'موکل',
                'verbose_name_plural': 'موکل ها',
            },
        ),
    ]
