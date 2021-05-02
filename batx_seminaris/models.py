from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Departament(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Seminari(models.Model):
    nom = models.CharField(max_length=100)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    places = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom


class Solicitud(models.Model):
    plantajament = models.TextField()
    seminari = models.ForeignKey(Seminari, on_delete=models.CASCADE)
    usuari = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    assignat = models.BooleanField(default=False)

   
