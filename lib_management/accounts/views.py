from django.shortcuts import render
from .forms import LoginForm
from .models import User
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == "POST":
        roll_no = request.POST['roll_no']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        dept = request.POST['dept']
        
        user = User.objects.create_user(roll_no=roll_no,password = password,name = name,email = email,dept = dept)
        return HttpResponse("hello"+user.name)
    else:
        form = LoginForm()
        return render(request,'accounts/signup.html',{
            'form':form
        })


def login(request):
    return render(request,'accounts/login.html')