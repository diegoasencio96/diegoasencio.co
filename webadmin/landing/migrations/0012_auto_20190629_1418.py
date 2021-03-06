# Generated by Django 2.2.2 on 2019-06-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20190629_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'ordering': ['order'], 'verbose_name': 'Acerca de mi', 'verbose_name_plural': 'Acerca de mi'},
        ),
        migrations.AlterModelOptions(
            name='clientreview',
            options={'ordering': ['order'], 'verbose_name': 'Comentario de cliente', 'verbose_name_plural': 'Comentarios de clientes'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['order'], 'verbose_name': 'Educación', 'verbose_name_plural': 'Educación'},
        ),
        migrations.AlterModelOptions(
            name='entrepreneurial',
            options={'ordering': ['order'], 'verbose_name': 'Emprendimiento', 'verbose_name_plural': 'Emprendimientos'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['order'], 'verbose_name': 'Institución', 'verbose_name_plural': 'Instituciones'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['order'], 'verbose_name': 'Experiencia laboral', 'verbose_name_plural': 'Experiencias laborales'},
        ),
        migrations.AlterModelOptions(
            name='professionalskill',
            options={'ordering': ['order'], 'verbose_name': 'Habilidad profesional', 'verbose_name_plural': 'Habilidades profesionales'},
        ),
        migrations.AlterModelOptions(
            name='projectcategory',
            options={'ordering': ['order'], 'verbose_name': 'Categoría de proyecto', 'verbose_name_plural': 'Categorías de proyectos'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order'], 'verbose_name': 'Lo que hago', 'verbose_name_plural': 'Lo que hago'},
        ),
        migrations.AlterModelOptions(
            name='siteconfig',
            options={'ordering': ['order'], 'verbose_name': 'Configuración del sitio', 'verbose_name_plural': 'Configuración del sitio'},
        ),
        migrations.AlterModelOptions(
            name='technicalskill',
            options={'ordering': ['order'], 'verbose_name': 'Habilidad técnica', 'verbose_name_plural': 'Habilidades técnicas'},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['order'], 'verbose_name': 'Experiencia laboral', 'verbose_name_plural': 'Experiencias laborales'},
        ),
        migrations.AddField(
            model_name='aboutme',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='clientreview',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='education',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='entrepreneurial',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='institution',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='professionalskill',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='projectcategory',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='technicalskill',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
