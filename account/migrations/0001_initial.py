# Generated by Django 3.2.4 on 2021-06-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('activation_code', models.CharField(blank=True, max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]