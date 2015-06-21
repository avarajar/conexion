from django.db import models
from django.template.defaultfilters import slugify
from colorfield.fields import ColorField


class Co_Creadore(models.Model):
    nombre = models.CharField(max_length=144)
    imagen = models.ImageField(upload_to='imagenes_co_creadores', null=True, blank=True)
    perfil = models.TextField(help_text='Descripcion del Co_Creador', default='')
    twitter = models.URLField()
    linkedin = models.URLField()
    facebook = models.URLField()

    def __unicode__(self):
        return u"%s" % self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super(Co_Creadore, self).save(*args, **kwargs)


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, default='')

    def __unicode__(self):
        return u"%s" % self.tag

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        super(Tag, self).save(*args, **kwargs)


class Dinamica(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    type_CHOICES = (
                   ('1', 'Global'),
                   ('2', 'Free'),
                   ('3', 'Premium'),
                   )
    tipo_usuario = models.CharField(max_length=100, verbose_name="Seleccione tipo de usuario", choices=type_CHOICES)
    type_CHOICES1 = (
                   ('1', 'Individual'),
                   ('2', 'Grupal'),
                   )
    tipo_dinamica = models.CharField(max_length=100, verbose_name="Seleccione tipo de dinamica", choices=type_CHOICES1)
    limite_participantes = models.IntegerField()
    tiempo_desarrollo = models.TimeField()
    descripcion = models.TextField(help_text='Descripcion de la dinamica', default='')
    objetivo_general = models.CharField(max_length=250, null=True, blank=True)
    objetivo_especifico_uno = models.CharField(max_length=250, null=True, blank=True)
    objetivo_especifico_dos = models.CharField(max_length=250, null=True, blank=True)
    objetivo_especifico_tres = models.CharField(max_length=250, null=True, blank=True)
    tags = models.ForeignKey(Tag)
    imagen_uno = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_dos = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_tres = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_cuatro = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_cinco = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_seis = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_siete = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_ocho = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_nueve = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    imagen_diez = models.ImageField(upload_to='imagenes_dinamicas/', null=True, blank=True)
    slug = models.SlugField(max_length=250, blank=True, default='')

    def __unicode__(self):
        return u"%s" % self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Dinamica, self).save(*args, **kwargs)


class Reto(models.Model):
    nombre = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes_retos/', null=True, blank=True)
    participantes = models.IntegerField()
    duracion = models.TimeField()
    descripcion = models.TextField(help_text='Descripcion del Reto ', default='')
    objetivo_general = models.CharField(max_length=250, null=True, blank=True)
    objetivo_especifico_uno = models.CharField(max_length=250, null=True, blank=True)
    objetivo_especifico_dos = models.CharField(max_length=250, null=True, blank=True)
    objetivo_especifico_tres = models.CharField(max_length=250, null=True, blank=True)
    recompensa = models.TextField(help_text='Recompensa del Reto', default='')
    evidencias = models.DateTimeField()
    aprendizajes = models.DateTimeField()
    soluciones = models.DateTimeField()
    resultados = models.DateTimeField()
