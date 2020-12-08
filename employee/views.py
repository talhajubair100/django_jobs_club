from django.shortcuts import redirect, render
from .forms import EmployeCreationForm
from django.contrib.auth.models import User
from .models import EmployeUser
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def employe_create_view(request):
    employe_profile = EmployeUser.objects.get(emp_user=request.user)
    form = EmployeCreationForm(instance=employe_profile)
    if request.method == 'POST':
        form = EmployeCreationForm(request.POST, request.FILES, instance=employe_profile)
        if form.is_valid():
            form.save()
            return redirect('employe_add')
    return render(request, 'employe_create.html', {'form': form})
