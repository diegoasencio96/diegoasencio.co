# Generated by Django 2.2.2 on 2019-07-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_auto_20190630_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(default=1, max_length=60, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
