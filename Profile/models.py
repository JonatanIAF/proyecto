from django.db import models

# Create your models here.
#from django.db import models
from django.utils import timezone
# Create your models here.

class CiudadM(models.Model):
    ciudad = models.CharField(max_length=254, null = False)

class GeneroM(models.Model):
    genero = models.CharField(max_length=254, null = False)

class OcupacionM(models.Model):
    ocupacion = models.CharField(max_length=254, null = False)

class EstadoM(models.Model):
    estado = models.CharField(max_length=254, null = False)

class Estado_civilM(models.Model):
    estado_civil = models.CharField(max_length=254, null = False)

class ProfileP(models.Model):
    nombre = models.CharField(max_length=254, null = False)
    apPat = models.CharField(max_length=254, null = False)
    apMat = models.CharField(max_length=254, null = False)
    edad = models.IntegerField(null = False)

    ciudad = models.ForeignKey(CiudadM, on_delete = models.CASCADE)
    genero = models.ForeignKey(GeneroM, on_delete = models.CASCADE)
    ocupacion = models.ForeignKey(OcupacionM, on_delete = models.CASCADE)
    estado = models.ForeignKey(EstadoM, on_delete = models.CASCADE)
    estado_civil = models.ForeignKey(Estado_civilM, on_delete = models.CASCADE)
    
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)





# class ModelEstado(models.Model):
#     estado = models.ForeignKey(ProfileP, on_delete = models.CASCADE)

    def str(self):
        return self.name

    class Meta: 
        db_table = 'ProfileP'