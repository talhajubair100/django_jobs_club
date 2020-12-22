from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import CompanyCreationForm
from .models import CompanyUser

# Create your views here.

def company_create_view(request):
    company_profile = CompanyUser.objects.get(com_user=request.user)
    form = CompanyCreationForm()
    context = {'form': form, 'company_profile': company_profile}
    return render(request, 'company_create.html', context)
