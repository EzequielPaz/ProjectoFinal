from django.db import models

# Create your models here.
class Postear(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return self.title