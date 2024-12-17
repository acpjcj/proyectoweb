from django.db import models



# Create your models here.
class Project(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=200, verbose_name="Autor")
    
    published = models.DateField(verbose_name="Fecha de publicación")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    url = models.URLField(verbose_name="URL", null=True, blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created']

    def __str__(self):
        return self.title
