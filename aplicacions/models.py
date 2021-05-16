from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group , User
from .modelManagers import LListaAplicacions


class Aplicacio(models.Model):
    nom = models.CharField(max_length=30)
    descripcio = models.CharField(max_length=200)
    data_limit_inici = models.DateField()
    data_limit_fi = models.DateField()
    url_acces = models.CharField(max_length=60,blank=True)
    url_backend = models.CharField(max_length=60,blank=True)
    llista_grups = models.ManyToManyField(Group)
    llista_encarregats = models.ManyToManyField(User,limit_choices_to={"rol__id_rol":1}) 

    llistatAplicacions= LListaAplicacions()

    class Meta:
        verbose_name_plural = 'Aplicacions'

    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        if self.data_limit_inici > self.data_limit_fi:
            raise ValidationError(
                "La Data inici no pot ser mes gran que la fi")
        super(Aplicacio, self).save(*args, **kwargs)
