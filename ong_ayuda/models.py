from django.db import models

# Create your models here.
class Especie(models.Model):
    nombre_especie = models.CharField(primary_key=True,max_length=60)

    def __str__(self):
        return self.nombre_especie

class Mascota(models.Model):
    chip = models.CharField(primary_key=True,max_length=60)
    nombre = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='fotos')
    edad = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    esterilizado = models.CharField(max_length=60)
    nombre_especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre