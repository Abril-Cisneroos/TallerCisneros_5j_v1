from django.db import models

# Create your models here.

class AlumnoT(models.Models):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
