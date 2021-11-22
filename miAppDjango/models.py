from django.db import models

# Create your models here.
class Persona ( models.Model ):
    nombre = models.CharField( max_length=100)
    telefono =models.CharField( max_length=100)
    email = models.CharField( max_length=50)

    def __str__(self):
        return str(self.id)+","+self.nombre+","+self.telefono+","+self.email

class Car ( models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    #many to many
    #persona = models.ManyToManyField(Persona)
    color = models.CharField( max_length=20)
    placa = models.IntegerField
    fabricante = models.CharField( max_length=50)
    modelo = models.CharField( max_length=30)
    kilometraje = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)+","+self.color+","+self.placa+","+self.modelo