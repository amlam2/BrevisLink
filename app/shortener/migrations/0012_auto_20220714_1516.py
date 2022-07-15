# Generated by Django 3.2.9 on 2022-07-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0011_alter_urlentry_url_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlentry',
            name='url_short',
            field=models.URLField(unique=True, verbose_name='Короткая ссылка'),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='url_text',
            field=models.URLField(unique=True, verbose_name='Полная ссылка'),
        ),
    ]
