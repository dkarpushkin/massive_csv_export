# Generated by Django 2.2.1 on 2019-05-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS plpython3u;', 'DROP EXTENSION plpython3u CASCADE;'),
    ]