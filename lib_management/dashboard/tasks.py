from home.models import Student
from celery import shared_task
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages


@shared_task
def add(x, y):
    print("addition of 2 numbers is", x+y)


@shared_task
def send_email(request, subject, body, mail):
    print("in tasks....send_email")
    try:
        e_mail = EmailMessage(
            subject,  # subject
            body,  # body
            'dhanushkumarganapathy@outlook.com',  # host_email,
            [mail, ],  # receiver
        )
        e_mail.fail_silently = False
        e_mail.send()
        #messages.success(request, "Mail sent successfully")
    except:
        #messages.error(request, "Mail couldn't be sent, pls try after some time")
        pass

# @shared_task
# def send_mail(request):  # should not wait until mail is sent

#     if request.session.get('roll_no'):
#         student = Student.objects.get(roll_no=request.session['roll_no'])
#         if student.is_admin:
#             if request.method == "POST" and 'damage' in request.POST:
#                 book_id = request.POST.get('book_id')
#                 copy_no = request.POST.get('copy_no')
#                 roll_no = request.POST.get('roll_no')
#                 email = Student.objects.get(roll_no=roll_no)
#                 email = email.mail
#                 print(book_id, copy_no, roll_no, email, sep="\n")
#                 return render(request, 'dashboard/send_mail.html', {'student': student, 'book_id': book_id,
#                                                                     'copy_no': copy_no, 'roll_no': roll_no,
#                                                                     'email': email})
#             elif request.method == "POST" and 'mail' in request.POST:
#                 mail = request.POST.get('email')
#                 subject = request.POST.get('subject')
#                 body = request.POST.get('body')
#                 try:
#                     e_mail = EmailMessage(
#                         subject,  # subject
#                         body,  # body
#                         'dhanushkumarganapathy@outlook.com',  # host_email,
#                         [mail, ],  # receiver
#                     )
#                     e_mail.fail_silently = False
#                     e_mail.send()
#                     messages.success(request, "Mail sent successfully")
#                 except:
#                     messages.error(
#                         request, "Mail couldn't be sent, pls try after some time")
#                     pass
#                 return redirect('/me/view-damage')
#             else:
#                 return redirect('/me/view-damage')

#         else:
#             return redirect('/me')

#     else:
#         return redirect('/me')
