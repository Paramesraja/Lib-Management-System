from django.db import models


# Create your models here.
class Student(models.Model):
    roll_no = models.TextField(primary_key=True, verbose_name="Roll No", max_length=8,
                               unique=True, blank=False)
    name = models.TextField(verbose_name="name", max_length=255, blank=False)
    mail = models.EmailField(verbose_name="Email", blank=False)
    linkedin = models.URLField(verbose_name="Linkedin")
    photo = models.ImageField(verbose_name="Avatar", upload_to='images')
    dept = models.TextField(verbose_name="Department", blank=False)
    phone = models.CharField(verbose_name="Phone", max_length=10, blank=True)
    twitter = models.URLField(verbose_name="Twitter", blank=True)
    facebook = models.URLField(verbose_name="Facebook", blank=True)
    instagram = models.URLField(verbose_name="Instagram", blank=True)
    about = models.TextField(verbose_name="About", blank=True)
    date_joined = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login")
    is_admin = models.BooleanField(verbose_name="Is Admin", default=False)

    def __str__(self):
        return self.name + " " + self.roll_no


class Donate(models.Model):
    status_choices = [
        (1, "Success"),
        (0, "Failed")
    ]
    razorpay_order_id = models.CharField(verbose_name="Razorpay Order id", primary_key=True, max_length=255)
    razorpay_payment_id = models.CharField(verbose_name="Razorpay Payment id", max_length=255, blank=True)
    razorpay_signature = models.CharField(verbose_name="Razorpay signature", max_length=255, blank=True)
    date_donated = models.DateTimeField(verbose_name="Date", blank=True,null=True)
    amount = models.CharField(verbose_name="Amount", max_length=255)
    name = models.CharField(verbose_name="Name", max_length=255)
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(verbose_name="Phone", max_length=10)
    status = models.CharField(verbose_name="Payment status", choices=status_choices, max_length=255,blank=True)

    def __str__(self):
        return self.name + " " + self.amount
