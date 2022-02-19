from social_core.pipeline.partial import partial
from django.shortcuts import redirect, render
from .models import Student
import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@partial
def create_user(backend, response, *args, **kwargs):
    request = kwargs.get('request')
    roll_no = response['family_name']
    name = response['given_name']
    email = response['upn']
    dept = email[-12:-10]
    dept = dept.upper()
    try:
        last_login = datetime.datetime.now()
        user = Student.objects.get(roll_no=roll_no)
        user.last_login = last_login
        user.save()
        request.session['roll_no'] = user.roll_no
        return
    except Student.DoesNotExist:
        if request.method == "POST":
            linkedin = request.POST.get('linkedin')
            last_login = datetime.datetime.now()
            user = Student.objects.create(roll_no=roll_no, name=name, mail=email, dept=dept, linkedin=linkedin,
                                          last_login=last_login)
            try:
                template = render_to_string('home/email.html', {'name': name})
                e_mail = EmailMessage(
                    'Thanks for creating an account in Kart.',  # subject
                    template,  # body
                    'dhanushkumarganapathy@outlook.com',  # host_email,
                    [email],  # receiver
                )
                e_mail.fail_silently = False
                e_mail.send()
            except Exception:
                pass
            request.session['roll_no'] = user.roll_no
            return

        else:
            return render(request, 'home/signup.html', {'roll_no': roll_no, 'name': name, 'email': email, 'dept': dept})
