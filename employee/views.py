from django.http.response import JsonResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .forms import EmployeCreationForm
from django.contrib.auth.models import User
from .models import EmployeUser
from django.contrib.auth.decorators import login_required
from address .models import District, Division
from .forms import forms
# Create your views here.
@login_required
def employe_create_view(request):
    employe_profile = EmployeUser.objects.get(emp_user=request.user)

    if employe_profile.district is None:

        form = EmployeCreationForm()
        if request.method == 'POST':
            form = EmployeCreationForm(request.POST, request.FILES, instance=employe_profile)
            if form.is_valid():
                employeuser = form.save(commit=False)
                employeuser.emp_user = request.user
                employeuser.save()
                return redirect('/')
        return render(request, 'employe_create.html', {'form': form, 'employe_profile': employe_profile})
    else:
        return redirect('employe_change')


@login_required
def employe_update_view(request):
    employe_profile = EmployeUser.objects.get(emp_user=request.user)
    if employe_profile.district:

        form = EmployeCreationForm(instance=employe_profile)
        if request.method == 'POST':
            form = EmployeCreationForm(request.POST, request.FILES, instance=employe_profile)
            if form.is_valid():
                form.save()
                return redirect('employe_change')
        return render(request, 'employe_create.html', {'form': form, 'employe_profile': employe_profile})
    else:
       return redirect('employe_add')

# AJAX
def load_district(request):
    division_id = request.GET.get('division_id')
    districts = District.objects.filter(division_id=division_id)
    #return render(request, 'districts_dropdown_list_options.html', {'districts': districts})
    print(list(districts.values('id', 'name')))
    return JsonResponse(list(districts.values('id', 'name')), safe=False)