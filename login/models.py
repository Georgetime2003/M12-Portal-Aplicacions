from django.db import models
from django.contrib.auth.models import Group

class Curs(models.Model):
   nom = models.CharField(max_length=60)
   
   def __str__(self):
        return self.nom

class Group(Group):
    curs = models.ForeignKey(Curs, on_delete=models.CASCADE)



