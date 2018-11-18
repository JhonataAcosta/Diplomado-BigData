from django.db import models

# Create your models here.
class Estudiante (models.Model):
    nombres=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.CharField(max_length=10)