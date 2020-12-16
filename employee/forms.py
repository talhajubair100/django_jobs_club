from django import forms
from address.models import District, Division
from .models import EmployeUser


class EmployeCreationForm(forms.ModelForm):
    class Meta:
        model = EmployeUser
        exclude = ('emp_user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()

        if 'division' in self.data:
            try:
                division_id = int(self.data.get('division'))
                self.fields['district'].queryset = District.objects.filter(division_id=division_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['district'].queryset = self.instance.division.district_set.order_by('name')
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.division.district_set.order_by('name')
            

# contry = Division
# city = District            