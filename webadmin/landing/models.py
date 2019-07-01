from django.db import models

from django.template.defaultfilters import slugify
# Create your models here.


class SiteConfig(models.Model):
    image = models.ImageField(upload_to="site-config/", verbose_name="Imágen")
    title = models.CharField(max_length=30, verbose_name="Título del sítio")
    person = models.CharField(max_length=60, verbose_name="Nombre de la persona")
    job_title = models.CharField(max_length=60, verbose_name="Título o cargo de la persona")
    email = models.EmailField(max_length=40, verbose_name="Correo electrónico de la persona")
    cellphone = models.CharField(max_length=12, verbose_name="Teléfono ó Celular de la persona")
    address = models.CharField(max_length=100, verbose_name="Dirección o lugar de ubicación de la persona")
    copyright = models.CharField(max_length=150, verbose_name="Derechos de autor")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Configuración del sitio'
        verbose_name_plural = 'Configuración del sitio'


class SocialNetwork(models.Model):
    icon = models.CharField(max_length=20, verbose_name="Icono de la red social")
    name = models.CharField(max_length=20, verbose_name="Nombre de la red social")
    url = models.URLField(max_length=60, verbose_name="URL de la red social")
    order = models.PositiveIntegerField(verbose_name="Orden")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'


class TechnicalSkill(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    score = models.PositiveIntegerField(verbose_name="Puntaje (%)", default=0)
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Habilidad técnica'
        verbose_name_plural = 'Habilidades técnicas'


class ProfessionalSkill(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    score = models.PositiveIntegerField(verbose_name="Puntaje (%)", default=0)
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Habilidad profesional'
        verbose_name_plural = 'Habilidades profesionales'


class AboutMe(models.Model):
    image = models.ImageField(upload_to="about-me/", verbose_name="Imágen")
    title = models.CharField(max_length=20, verbose_name="Título")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    curriculum_vitae = models.FileField(upload_to="about-me/", verbose_name="Hoja de vida")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Acerca de mi'
        verbose_name_plural = 'Acerca de mi'


class Service(models.Model):
    icon = models.CharField(max_length=30, verbose_name="Icono")
    title = models.CharField(max_length=30, verbose_name="Título")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Lo que hago'
        verbose_name_plural = 'Lo que hago'


class ProjectCategory(models.Model):
    title = models.CharField(max_length=30, verbose_name="Título")
    slug = models.CharField(max_length=200, blank=True, verbose_name="Slug")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProjectCategory, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Categoría de proyecto'
        verbose_name_plural = 'Categorías de proyectos'


class Entrepreneurial(models.Model):
    category = models.ForeignKey(ProjectCategory, verbose_name="Categoría de proyecto", on_delete=models.PROTECT)
    image = models.ImageField(upload_to="about-me/", verbose_name="Imágen")
    title = models.CharField(max_length=30, verbose_name="Título")
    subtitle = models.CharField(max_length=60, verbose_name="Subtítulo")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    url = models.URLField(max_length=60, verbose_name="URL")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Emprendimiento'
        verbose_name_plural = 'Emprendimientos'


class Institution(models.Model):
    TI = (
        ('E', 'Educación'),
        ('T', 'Corporación')
    )
    name = models.CharField(max_length=60, verbose_name="Nombre")
    type = models.CharField(max_length=10, verbose_name="Tipo de institución", choices=TI)
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'


class Education(models.Model):
    title = models.CharField(max_length=60, verbose_name="Título")
    institution = models.ForeignKey(Institution, verbose_name="Institución educativa", on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Educación'
        verbose_name_plural = 'Educación'


class WorkExperience(models.Model):
    title = models.CharField(max_length=60, verbose_name="Título")
    institution = models.ForeignKey(Institution, verbose_name="Institución Laboral", on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Experiencia laboral'
        verbose_name_plural = 'Experiencias laborales'


class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio/", verbose_name="Imágen")
    title = models.CharField(max_length=60, verbose_name="Título")
    category = models.ForeignKey(ProjectCategory, verbose_name="Categoría de proyecto", on_delete=models.PROTECT)
    description = models.TextField(max_length=300, verbose_name="Descripción")
    technical_skills = models.ManyToManyField(TechnicalSkill, verbose_name="Tecnologías o herramientas")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolio'


class ClientReview(models.Model):
    image = models.ImageField(upload_to="client_review/", verbose_name="Imágen")
    name = models.CharField(max_length=60, verbose_name="Nombre")
    job_title = models.CharField(max_length=80, verbose_name="Cargo")
    review = models.TextField(max_length=300, verbose_name="Comentario")
    order = models.PositiveIntegerField(verbose_name="Orden", default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Comentario de cliente'
        verbose_name_plural = 'Comentarios de clientes'


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=60, verbose_name="Nombres")
    last_name = models.CharField(max_length=60, verbose_name="Apellidos")
    email = models.EmailField(max_length=60, verbose_name="Correo electrónico")
    subject = models.CharField(max_length=70, verbose_name="Asunto")
    message = models.TextField(max_length=600, verbose_name="Mensaje")

    def __str__(self):
        return '{}'.format(self.subject)

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'
