# Generated by Django 2.2.2 on 2019-07-01 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_auto_20190629_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['order'], 'verbose_name': 'Portafolio', 'verbose_name_plural': 'Portafolio'},
        ),
        migrations.AddField(
            model_name='projectcategory',
            name='slug',
            field=models.CharField(blank=True, max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landing.Institution', verbose_name='Institución Laboral'),
        ),
    ]
