# Generated by Django 3.2.9 on 2022-07-14 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0008_auto_20220714_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlentry',
            name='url_id',
        ),
    ]
