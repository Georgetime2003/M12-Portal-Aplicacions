from django.db import models
from django.core.exceptions import ValidationError


class Aplicacio(models.Model):
    nom = models.CharField(max_length=30)
    descripcio = models.CharField(max_length=200)
    data_limit_inici = models.DateField()
    data_limit_fi = models.DateField()

    class Meta:
        verbose_name_plural = 'Aplicacions'

    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        if self.data_limit_inici > self.data_limit_fi:
            raise ValidationError(
                "La Data inici no pot ser mes gran que la fi")
        super(Aplicacio, self).save(*args, **kwargs)
