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


STATUS_CHOICES = (
    ('In Stock', 'In Stock'),
    ('Need Refill', 'Need Refill'),
    ('Out of Stock', 'Out of Stock'),
    ('Pending','Pending')
)


class InventoryForm(forms.ModelForm):
    number = forms.CharField(label='Item number', max_length=100)
    name = forms.CharField(label='Item name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(label='Item Category',choices=CATEGOY_CHOICES)
    qty = forms.IntegerField(label='Item qty')
    type = forms.ChoiceField(label='Item Type',choices=TYPES_CHOICES)
    status = forms.ChoiceField(label='Item Type',choices=STATUS_CHOICES)
    
    class Meta:
        model = Inventory
        exclude = ("user", )