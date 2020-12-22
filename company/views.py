from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import CompanyCreationForm
from .models import CompanyUser
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def company_create_view(request):
    company_profile = CompanyUser.objects.get(com_user=request.user)
    form = CompanyCreationForm()
    # if request.method == 'POST':
    #     form = CompanyCreationForm(request.POST)
    context = {'form': form, 'company_profile': company_profile}
    return render(request, 'company_create.html', context)
