from django import forms
from django.forms import ModelForm
from company.models import Employee , Department



class NewEmp(forms.ModelForm):
    class Meta:
     model=Employee
     fields = '__all__'


class NewDept(forms.ModelForm):

    class Meta:
     model=Department
     dec = forms.CharField(widget=forms.Textarea, max_length=400)
     fields = '__all__'






