from django import forms
from django.forms.forms import Form
from . import models


class LoginForm(forms.Form):
   linkedin = forms.URLField()

class DisplayForm(forms.Form):
    roll_no = forms.CharField(max_length=255,disabled=True,required=False)
    name = forms.CharField(max_length=255,disabled=True,required=False)
    email = forms.EmailField(disabled=True,required=False)
    dept = forms.CharField(max_length=255,disabled=True,required=False)
    

