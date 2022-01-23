from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your views here.


def addbooks(request):
    ord = Order.objects.all()
    book = Book.objects.all()
    return render(request, 'libr/addbooks.html', {'ord': ord, 'book': book})


def booktodb(request):

    bookid = request.POST['bookid']
    isbnnum = request.POST['isbnnum']
    bookname = request.POST['bookname']
    author = request.POST['author']
    domain = request.POST['domain']
    quantity = request.POST['quantity']

    bookadd = Book(bookid=bookid, isbnnum=isbnnum, bookname=bookname,
                   author=author, domain=domain, quantity=quantity,)
    bookadd.save()

    return render(request, 'libr/successmsg.html')


def booksview(request):
    allbooks = Book.objects.all()

    return render(request, 'libr/bookview.html', {'book_details': allbooks})
