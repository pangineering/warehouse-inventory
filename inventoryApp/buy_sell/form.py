from distutils.command.upload import upload
from django import forms
from .models import Purchase, Selling
from jsonfield.forms import JSONField
TEAM_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)
CATEGOY_CHOICES = (
    ('Manager', 'Manager'),
    ('Sales', 'Sales'),
    ('Engineer', 'Engineer'),
    ('Warehouse', 'Warehouse'),
)
STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Approve', 'Approve'),
    ('Complete', 'Complete'),
    ('Cancel', 'Cancel'),
    ('Revision', 'Revision'),
)

class PurchaseForm(forms.ModelForm):
    p_num = forms.CharField(label='Purchase number', max_length=100)
    name = forms.CharField(label='Product Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeInput()
    team = forms.ChoiceField(label='Purchase Team',choices=TEAM_CHOICES)
    status = forms.ChoiceField(label='Purchase Status',choices=STATUS_CHOICES)
    category = forms.ChoiceField(label='Purchase Category',choices=CATEGOY_CHOICES)
    item = forms.CharField(label='Purchase Item',max_length=200)
   
    class Meta:
        model = Purchase
        exclude = ("user","id","employee_number" )


class OrderForm(forms.ModelForm):
    s_num = forms.CharField(label='Order number', max_length=100)
    name = forms.CharField(label='Order number', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeInput()
    team = forms.ChoiceField(label='Order Team',choices=TEAM_CHOICES)
    status = forms.ChoiceField(label='Order Status',choices=STATUS_CHOICES)
    category = forms.ChoiceField(label='Order Category',choices=CATEGOY_CHOICES)
    item = forms.CharField(max_length=200)
   
    class Meta:
        model = Selling
        exclude = ("user","id")
