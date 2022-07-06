from turtle import position
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Employee

TEAM_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)
Position_CHOICES = (
    ('Manager', 'Manager'),
    ('Sales', 'Sales'),
    ('Engineer', 'Engineer'),
    ('Warehouse', 'Warehouse'),
)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class ProfileForm(forms.ModelForm):
    employee_number = forms.CharField(label='Employee Number')
    description = forms.CharField(widget=forms.Textarea)
    team = forms.ChoiceField(label='Employee Team',choices=TEAM_CHOICES)
    position = forms.ChoiceField(label='Employee Position',choices=Position_CHOICES)

   
    class Meta:
        model = Employee
        exclude = ("user","id" )