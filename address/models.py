from django.db import models

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class District(models.Model):
    divisions = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name