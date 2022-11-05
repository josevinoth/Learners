# from django import forms
# from ..models import Employee
#
# class EmployeeaddForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..models import User_extInfo
from django import forms


class EmpeditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','is_active','email','password']

class UserexteditForm(forms.ModelForm):
    class Meta:
        model = User_extInfo
        fields = ['emp_contact','emp_job_title','emp_no_of_employees','emp_interest','emp_free_text','emp_country','emp_status','emp_role']
        # fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(UserexteditForm,self).__init__(*args, **kwargs)
        self.fields['emp_status'].empty_label = "--Select--"
        self.fields['emp_role'].empty_label = "--Select--"


