# Generated by Django 2.2.2 on 2019-06-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20190629_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreview',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='clientreview',
            name='review',
            field=models.TextField(max_length=300, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='first_name',
            field=models.CharField(max_length=60, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='last_name',
            field=models.CharField(max_length=60, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='education',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='entrepreneurial',
            name='subtitle',
            field=models.CharField(max_length=60, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='entrepreneurial',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Título'),
        ),
    ]
