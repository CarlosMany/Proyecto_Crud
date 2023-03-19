from django.db import models

# Create your models here.

class Tarea2(models.Model):
    tarea2 = models.CharField(max_length=100)

    def __str__(self):
        return self.tarea2
    