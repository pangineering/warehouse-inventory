from distutils.command.upload import upload
from django import forms
from .models import Products

CATEGOY_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)

TYPES_CHOICES = (
    ('Standard', 'Standard'),
    ('Custom', 'Custom')
)

class ProductForm(forms.ModelForm):
    number = forms.CharField(label='Product number', max_length=100)
    name = forms.CharField(label='Product number', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(label='Product Category',choices=CATEGOY_CHOICES)
    qty = forms.IntegerField(label='Product Qty')
    type = forms.ChoiceField(label='Product Type',choices=TYPES_CHOICES)
    #img = forms.ImageField()

    class Meta:
        model = Products
        exclude = ("user", )