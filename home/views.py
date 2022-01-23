from django.shortcuts import render
from accounts.models import User
from django.contrib.auth import logout
from libr.models import *
# Create your views here.


def home(request):
    if request.method == 'POST':
        logout(request)
    try:
        user = request.user

    except User.DoesNotExist:
        print("executing")
        user = None

    try:

        ord = Order.objects.all()
        book = Book.objects.all()

    except:
        ord = {'bookid': 'None', 'orderid': 'None'}

    return render(request, 'home/index.html', {
        'user': user, 'ord': ord, 'book': book
    })
