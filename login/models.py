from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class Rol(models.Model):
    PROFESSOR = 1
    ALUMNE = 2
    
    ROLE_OPCIONS = (
        (PROFESSOR, 'Professor'),
        (ALUMNE, 'Alumne'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.PositiveSmallIntegerField(choices=ROLE_OPCIONS, blank=True, null=True)


class Curs(models.Model):
   nom = models.CharField(max_length=60)
   
   def __str__(self):
        return self.nom


class Group(Group):
    curs = models.ForeignKey(Curs, on_delete=models.CASCADE)



