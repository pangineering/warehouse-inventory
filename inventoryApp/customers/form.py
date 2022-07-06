from django import forms
from .models import Customers

class CustomerForm(forms.ModelForm):
    number = forms.CharField(label='Customer number', max_length=100)
    name = forms.CharField(label='Customer number', max_length=100)
    company_name = forms.CharField(label='Customer Company Name', max_length=100)
    email = forms.CharField(label='Customer Email', max_length=100)
    mobile = forms.CharField(label='Customer Mobile', max_length=100)
    status = forms.CharField(label='Customer Status', max_length=100)

    class Meta:
        model = Customers
        exclude = ("user", )