# Generated by Django 4.0.4 on 2022-05-07 10:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='urlentry',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urlentry',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leads',
            name='follow_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date when link was followed'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='follower_fromwhere',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='leads',
            name='follower_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='leads',
            name='follower_os_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='datetime_available_from',
            field=models.DateTimeField(verbose_name='url available from'),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='datetime_available_to',
            field=models.DateTimeField(verbose_name='url available to'),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='partner_ads',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='qr_code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='snapshot',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='url_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='urlentry',
            name='url_text',
            field=models.TextField(),
        ),
    ]
