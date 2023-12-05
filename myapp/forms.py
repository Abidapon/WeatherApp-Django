# myapp/forms.py
from django import forms

class CitySearchForm(forms.Form):
    city = forms.CharField(max_length=100, label='Enter City')
