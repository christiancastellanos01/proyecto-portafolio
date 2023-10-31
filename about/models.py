from django.db import models

# Create your models here.

# modelo de la formación académica


class Academic(models.Model):
    formation = models.CharField(max_length=50, verbose_name='Formación')
    title = models.CharField(max_length=150, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha Actualización')

    class Meta:
        verbose_name = 'académico'
        verbose_name_plural = 'académicos'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.formation

# modelo de los programas que manejo


class Skill(models.Model):
    title = models.CharField(max_length=50, verbose_name='titulo')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha Actualización')

    class Meta:
        verbose_name = 'habilidad'
        verbose_name_plural = 'habilidades'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
