from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CompanyUser(models.Model):
    com_user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank=True, null=True)


    def __str__(self):
        return self.com_user.username