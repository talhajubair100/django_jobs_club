from django import forms
from .models import CompanyUser

class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = CompanyUser
        exclude = ('com_user', )