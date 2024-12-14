from django import forms
from .models import Tumbler

class TumblerForm(forms.ModelForm):
    class Meta:
        model = Tumbler
        fields = ['name', 'size', 'image', 'description','price']
