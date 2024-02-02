from django.db import models

from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='proyectos/', null=True, blank=True)

    def __str__(self):
        return self.titulo
