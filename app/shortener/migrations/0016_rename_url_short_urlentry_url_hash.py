# Generated by Django 3.2.9 on 2022-07-14 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0015_rename_url_text_urlentry_full_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlentry',
            old_name='url_short',
            new_name='url_hash',
        ),
    ]