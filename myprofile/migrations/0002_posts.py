# Generated by Django 3.2.4 on 2021-08-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.TextField(max_length=30)),
                ('emails', models.TextField(max_length=20)),
                ('comments', models.TextField(max_length=50)),
            ],
        ),
    ]
