from django.shortcuts import render
from accounts.models import User
from django.contrib.auth import logout

# Create your views here.
def home(request):
    if request.method == 'POST':
        logout(request)
    try:
        user = request.user
    except User.DoesNotExist:
        print("executing")
        user = None

    return render(request,'home/index.html',{
        'user':user
    })