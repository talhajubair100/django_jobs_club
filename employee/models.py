from django.db import models
from django.contrib.auth.models import User
from address.models import District, Division

# Create your models here.

class EmployeUser(models.Model):
    emp_user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank=True, null=True)
    photo = models.ImageField(upload_to='employe-photos/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender_choice = (
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        )
    gender = models.CharField(choices=gender_choice, max_length=10, blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    full_address = models.TextField(blank=True, null=True)
    cv = models.FileField(upload_to='documents/', null=True, blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.emp_user.username
