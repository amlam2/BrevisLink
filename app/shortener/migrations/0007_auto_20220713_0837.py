# Generated by Django 3.2.9 on 2022-07-13 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_alter_leads_urlentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlentry',
            name='qr_code',
        ),
        migrations.RemoveField(
            model_name='urlentry',
            name='snapshot',
        ),
    ]
