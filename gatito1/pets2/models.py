from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def _str_(self):
        return self.nombre

