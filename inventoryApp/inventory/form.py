from django import forms
from .models import Inventory

# Create your models here.
CATEGOY_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)

TYPES_CHOICES = (
    ('Buy', 'Buy'),
    ('Sell', 'Sell')
)

class InventoryForm(forms.ModelForm):
    number = forms.CharField(label='Item number', max_length=100)
    name = forms.CharField(label='Item name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(label='Item Category',choices=CATEGOY_CHOICES)
    qty = forms.IntegerField(label='Item qty')
    type = forms.ChoiceField(label='Item Type',choices=TYPES_CHOICES)
    status = forms.CharField(label='Item Status', max_length=100)
    class Meta:
        model = Inventory
        exclude = ("user", )