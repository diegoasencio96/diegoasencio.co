from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class PublicationCategory(models.Model):
    title = models.CharField(max_length=30, verbose_name="Título")

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Categoría de publicación'
        verbose_name_plural = 'Categorías de publicaciones'


class Publication(models.Model):
    image = models.ImageField(upload_to="publication/")
    title = models.CharField(max_length=50, verbose_name="Título")
    description = models.TextField(max_length=300, verbose_name="Descripción corta")
    full_description = RichTextField(verbose_name="Descripción completa")
    create_date = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    update_date = models.DateField(verbose_name="Fecha de actualización", auto_now=True)
    categories = models.ManyToManyField(PublicationCategory, verbose_name="Categorías de publicación")
    author = models.ForeingKey('auth.User', verbose_name="Tecnologías o herramientas", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
