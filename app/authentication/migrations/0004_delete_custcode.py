# Generated by Django 3.2.9 on 2022-07-13 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_custcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Custcode',
        ),
    ]