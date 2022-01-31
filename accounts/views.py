from django.shortcuts import render
from .forms import *
from .models import User
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'accounts/login.html')

