from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ChangePasswordForm, ResetPasswordKeyForm, AddEmailForm
from django import forms
from employee.models import EmployeUser
from company.models import CompanyUser
from django import forms as d_forms
from django.contrib.auth.models import Group




class CustomeLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomeLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'
        })

class CustomeSetPassForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(CustomeSetPassForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

class CustomeChngPassForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomeChngPassForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })


class CustomeResetPassForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomeResetPassForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })

class CustomeAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(CustomeAddEmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })


class CustomeSignupForm(SignupForm):

    #company = forms.CharField(max_length=100, required=True)
    is_company = forms.BooleanField(label=("Signup As Company?"), required=False)

    def __init__(self, *args, **kwargs):
        super(CustomeSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['is_company'].widget.attrs.update({

        })

    def save(self, request):
        user = super(CustomeSignupForm, self).save(request)
        is_company = self.cleaned_data.pop('is_company')
        if is_company == True:
            print('it is comapny')
            group = Group.objects.get(name="company")
            user.groups.add(group)
            company_user = CompanyUser.objects.get_or_create(com_user=user)
        else:
            print('it is not a company')
            group = Group.objects.get(name="employee")
            user.groups.add(group)
            employe_user = EmployeUser.objects.get_or_create(emp_user=user)

        return user


