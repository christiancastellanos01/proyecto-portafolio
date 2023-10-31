from django.db import models

# Create your models here.


class Project(models.Model):
    # el verbose_name es como en la pagina de admin los campos del modelo aparecen en ingles por ejemplo title poder cambiarlo a español
    title = models.CharField(max_length=150, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    # el blank y true es para especificar de que este campo del modelo no son obligatorios
    link = models.URLField(max_length=200, blank=True,
                           null=True, verbose_name='Enlace')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha Actualización')

    class Meta:
        # para que en admin cambie el nombre del modelo en ingles a español
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        # ordering es para que muestre los registros de los modelos de forma ascendente
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
