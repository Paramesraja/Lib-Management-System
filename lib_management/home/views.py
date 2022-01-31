from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.session.get('roll_no'):
        return redirect('/me')
    else:
        return render(request, 'home/home.html')
