from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, roll_no, name,dept, email,linkedin, password=None):
        user = self.model(
            roll_no=roll_no,
            name=name,
            dept = dept,
            email=email,
            linkedin = linkedin)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, roll_no, dept ,name, email,linkedin, password=None):
        user = self.create_user(
            roll_no=roll_no,
            name=name,
            email=email,
            dept = dept,
            password=password,
            linkedin = linkedin
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    roll_no = models.TextField(
        verbose_name='Roll no', unique=True, blank=False)
    photo = models.ImageField(verbose_name='Profile photo')
    name = models.TextField(verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    linkedin = models.URLField(verbose_name='Linked in Profile')
    dept = models.TextField(verbose_name='Department')
    no_post = models.IntegerField(verbose_name='No of Posts', default=0)
    date_joined = models.DateTimeField(
        verbose_name="Date joined", auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'roll_no'
    REQUIRED_FIELDS = ['password', 'name', 'email', 'dept']

    objects = UserManager()

    def __str__(self):
        return self.roll_no

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_admin
