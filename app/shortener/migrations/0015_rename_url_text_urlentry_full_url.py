# Generated by Django 3.2.9 on 2022-07-14 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0014_auto_20220714_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlentry',
            old_name='url_text',
            new_name='full_url',
        ),
    ]
