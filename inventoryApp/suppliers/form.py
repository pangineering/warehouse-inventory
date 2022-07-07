from django import forms
from .models import Suppliers

class SupplierForm(forms.ModelForm):
    number = forms.CharField(label='Supplier Number', max_length=100)
    name = forms.CharField(label='Supplier Name', max_length=100)
    company_name = forms.CharField(label='Supplier Company Name', max_length=100)
    email = forms.CharField(label='Supplier Email', max_length=100)
    mobile = forms.CharField(label='Supplier Mobile', max_length=100)

    class Meta:
        model = Suppliers
        exclude = ("user", )