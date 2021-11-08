from django.db import models

class Product(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=20)
  precio = models.IntegerField(null=True)
  descripcion = models.TextField(null=True, blank=True)
  categoria = models.CharField(max_length=20)
  dimensiones = models.CharField(max_length=20)
  referencia = models.TextField(null=True, blank=True)
  foto = models.CharField(max_length=256)

  def __str__(self):
    return self.nombre

