from django.http import request
from .models import User
from django.shortcuts import redirect, render
from . import forms
from social_core.pipeline.partial import partial


@partial
def create_user(backend, response, *args, **kwargs):
    request = kwargs.get('request')
    roll_no = response['family_name']
    name = response['given_name']
    email = response['upn']
    dept = roll_no[3:5]

    try:
        user = User.objects.get(roll_no = roll_no)
    except User.DoesNotExist:
        user = None
    if user:
        request.user = user
        return {'user':user}
    else: 
        form2 = forms.DisplayForm(
            initial={'roll_no': roll_no, 'name': name, 'email': email, 'dept': dept})
        if request.method == "POST":
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                linkedin = form.cleaned_data['linkedin']
                user = User.objects.create_user(
                    roll_no=roll_no, dept=dept, name=name, email=email, linkedin=linkedin)
                user.save()
                return { 'user' : user}

        else:
            form = forms.LoginForm()
            return render(request, 'accounts/signup.html', {'form': form, 'form2': form2})
