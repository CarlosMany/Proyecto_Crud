from django.db import models

class Tarea(models.Model):
    tarea = models.CharField(max_length=100)

    def __str__(self):
        return self.tarea

class Tarea2(models.Model):
    tarea = models.CharField(max_length=100)

    def __str__(self):
        return self.tarea