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