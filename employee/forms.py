from django import forms

from .models import EmployeUser


class EmployeCreationForm(forms.ModelForm):
    class Meta:
        model = EmployeUser
        fields = '__all__'