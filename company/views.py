from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .forms import CompanyCreationForm
from .models import CompanyUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required
def company_create_view(request):
    company_profile = CompanyUser.objects.get(com_user=request.user)
    form = CompanyCreationForm()
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST, request.FILES, instance=company_profile)
        if form.is_valid():
            companyuser = form.save(commit=False)
            companyuser.com_user = request.user
            companyuser.save()
            messages.success(request,'Good job! You successfully showed a SweetAlert message')
            return redirect('/')

    context = {'form': form, 'company_profile': company_profile}
    return render(request, 'company_create.html', context)
