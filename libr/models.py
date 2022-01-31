

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class Book(models.Model):
    bookid = models.CharField(max_length=8, primary_key=True, null=False)
    isbnnum = models.CharField(max_length=10)
    bookname = models.CharField(max_length=40, null=False)
    author = models.CharField(max_length=25)
    domain = models.CharField(max_length=20)

    quantity = models.IntegerField()


class Order(models.Model):
    orderid = models.CharField(max_length=8, primary_key=True, null=False)
    roll_no = models.ForeignKey(User, on_delete=models.CASCADE)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    issuedate = models.DateTimeField(default=timezone.now)
    duedate = models.DateTimeField()
    returndate = models.DateTimeField()
    received = models.IntegerField()
    returned = models.IntegerField()
