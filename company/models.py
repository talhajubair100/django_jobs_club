from django.db import models
from django.contrib.auth.models import User
from address.models import District, Division
# Create your models here.

class CompanyUser(models.Model):
    com_user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank=True, null=True)
    comapny_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    telephone = models.CharField(max_length=14, blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    full_address = models.TextField(blank=True, null=True)
    company_link = models.URLField(max_length=200, blank=True, null=True, unique=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True, unique=True)
    linkdin_link = models.URLField(max_length=200, blank=True, null=True, unique=True)
    

    def __str__(self):
        return self.com_user.username