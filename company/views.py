from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import CompanyCreationForm

# Create your views here.

def company_create_view(request):
    
    form = CompanyCreationForm()
    context = {'form': form}
    return render(request, 'company_create.html', context)
