from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from . models import User

class MyBackend(BaseBackend):
    def authenticate(self,request,roll_no,password):
        try: 
            user = User.objects.get(pk = roll_no)
            if check_password(password,user.password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, roll_no) :
        try:
            return User.objects.get(pk=roll_no)
        except User.DoesNotExist:
            return None
