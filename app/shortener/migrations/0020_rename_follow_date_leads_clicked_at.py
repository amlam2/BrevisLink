# Generated by Django 3.2.9 on 2022-07-14 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0019_rename_create_date_urlentry_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leads',
            old_name='follow_date',
            new_name='clicked_at',
        ),
    ]