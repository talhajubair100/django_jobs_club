from django.http.response import JsonResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .forms import EmployeCreationForm
from django.contrib.auth.models import User
from .models import EmployeUser
from django.contrib.auth.decorators import login_required
from address .models import District, Division

# Create your views here.
@login_required
def employe_create_view(request):
    employe_profile = EmployeUser.objects.get_or_create(emp_user=request.user)
    form = EmployeCreationForm(instance=employe_profile)
    if request.method == 'POST':
        form = EmployeCreationForm(request.POST, request.FILES, instance=employe_profile)
        if form.is_valid():
            form.save()
            return redirect('employe_add')
    return render(request, 'employe_create.html', {'form': form})

@login_required
def employe_update_view(request, pk):
    employe = get_object_or_404(EmployeUser, pk=pk)
    form = EmployeCreationForm(instance=employe)
    if request.method == 'POST':
        form = EmployeCreationForm(request.POST, request.FILES, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('employe_change', pk=pk)
    return render(request, 'employe_create.html', {'form': form})


# AJAX
def load_district(request):
    division_id = request.GET.get('division_id')
    districts = District.objects.filter(division_id=division_id)
    #return render(request, 'districts_dropdown_list_options.html', {'districts': districts})
    print(list(districts.values('id', 'name')))
    return JsonResponse(list(districts.values('id', 'name')), safe=False)