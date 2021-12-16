from django.forms import ModelForm
from . import models


class LoginForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['roll_no', 'password', 'photo',
                  'name', 'email', 'dept']
