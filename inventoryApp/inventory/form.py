from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    number = forms.CharField(label='Item number', max_length=100)
    name = forms.CharField(label='Item name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(label='Item Category', max_length=100)
    qty = forms.IntegerField(label='Item qty')
    type = forms.CharField(label='Item Type', max_length=100)
    status = forms.CharField(label='Item Status', max_length=100)
    class Meta:
        model = Inventory
        exclude = ("user", )