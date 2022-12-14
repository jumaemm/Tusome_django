# Generated by Django 4.1 on 2022-09-14 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusome_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='upload_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 14, 8, 18, 25, 292997, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='review',
            name='written_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 14, 8, 18, 25, 293997, tzinfo=datetime.timezone.utc)),
        ),
    ]
