# Generated by Django 2.2.2 on 2019-06-29 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20190629_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialnetwork',
            options={'ordering': ['pk'], 'verbose_name': 'Red social', 'verbose_name_plural': 'Redes sociales'},
        ),
    ]