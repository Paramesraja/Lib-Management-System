from django.shortcuts import render, redirect
from django.contrib.auth import logout
from home.models import Student
from django.contrib import messages
from .models import *
import json
import datetime
from django.core.mail import EmailMessage
import csv

from datetime import timedelta, date
from dashboard.tasks import send_email

# Create your views here.


def dashboard(request):  # to be added - a person cannot have two copies of same book
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_admin:
            if request.method == "POST" and 'issue' in request.POST:
                roll_no = request.POST.get('roll_no')
                book_id = request.POST.get('book_id')
                copy_no = request.POST.get('copy_no')

                iss = Issue.objects.raw(
                    "select id,count(*) as cou from dashboard_issue where roll_no = '" + roll_no + "' and date_returned is null;")[
                    0]
                if iss.cou == 2:
                    messages.error(request, roll_no +
                                   " has already taken two books")
                else:
                    try:
                        check = Copy.objects.raw(
                            "select id, status from dashboard_copy where bookid_id = " + book_id + " and copy_no = " + copy_no +
                            ";")[0]
                        if check.status == 'Not Available':
                            messages.error(request,
                                           "Copy number " + copy_no + " of bookid " + book_id + " is not available")
                        elif check.status == 'Damaged':
                            messages.error(request,
                                           "Copy number " + copy_no + " of bookid " + book_id + " has been reported damage please check")
                        else:
                            book = Book.objects.get(bookid=book_id)
                            issue = Issue(
                                bookid=book, roll_no=roll_no, copy_no=copy_no)
                            issue.save()
                            messages.success(request,
                                             "Copy number " + copy_no + " of bookid " + book_id + " has been issued successfully to " + roll_no)
                            copy = Copy.objects.filter(
                                bookid=book_id, copy_no=copy_no)[0]
                            copy.status = 'Not Available'
                            copy.save()
                    except:
                        messages.error(request, "No such book exists.")
            elif request.method == "POST" and 'backtolib' in request.POST:
                roll_no = request.POST.get('roll_no')
                book_id = request.POST.get('book_id')
                copy_no = request.POST.get('copy_no')
                # try:
                iss = Issue.objects.get(
                    roll_no=roll_no, bookid=book_id, copy_no=copy_no, date_returned=None)
                iss.date_returned = datetime.date.today()
                iss.save()
                book_copy = Copy.objects.get(bookid=book_id, copy_no=copy_no)
                book_copy.status = 'Available'
                book_copy.save()
                messages.success(request, "Book returned successfully")
                # except:
                #     messages.error(request,roll_no + " has not issued the " + book_id + " book")

            to_be_returned = Issue.objects.filter(
                date_issued=date.today() - timedelta(days=2))

            notyetreturned = Issue.objects.all()
            d = {}
            intindex = 0
            for i in notyetreturned:

                stringofindex = str(intindex)

                enddate = i.date_issued + timedelta(days=2)
                if((date.today()-enddate).days > 0):

                    d[stringofindex] = {
                        'rollno': i.roll_no,
                        'bookid': i.bookid.bookid,
                        'bookname': i.bookid.title,
                        'copynum': i.copy_no,
                        'renewed': i.renewed,
                        'dateissued': i.date_issued
                    }

                    intindex += 1

            # books that are in overdue
            return render(request, 'dashboard/ad_dashboard.html',
                          {'student': student, 'to_be_returned': to_be_returned, 'd': d})

        else:
            iss = Issue.objects.filter(
                roll_no=student.roll_no)
            d = {}
            intindex = 0
            for i in iss:

                stringofindex = str(intindex)
                if i.renewed == True:
                    duedate = i.date_issued + timedelta(days=30)
                else:
                    duedate = i.date_issued + timedelta(days=15)

                d[stringofindex] = {
                    'rollno': i.roll_no,
                    'bookid': i.bookid.bookid,
                    'bookname': i.bookid.title,
                    'copynum': i.copy_no,

                    'dateissued': i.date_issued,
                    'renewed': i.renewed,
                    'duedate': duedate,
                    'datereturned': i.date_returned,
                }

                intindex += 1
            return render(request, 'dashboard/dashboard.html', {'student': student, 'd': d})
    else:
        return redirect('/')


def log_out(request):
    logout(request)
    return redirect('/')


def renew(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if request.method == "POST":
            roll_no = student.roll_no
            book_id = request.POST.get('book_id')
            copy_no = request.POST.get('copy_no')

            try:
                iss = Issue.objects.get(
                    bookid=book_id, roll_no=roll_no, copy_no=copy_no, date_returned=None)
                if iss.renewed == False:
                    iss.renewed = True
                    iss.date_renewed = datetime.date.today()
                    iss.save()
                    messages.success(
                        request, "You have renewed the book successfully")
                else:
                    messages.error(
                        request, "You have renewed the book already")
            except:
                messages.error(request, "Invalid Details")
        return render(request, 'dashboard/renew.html', {'student': student})
    else:
        return redirect('/')


def profile(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if request.method == 'POST':
            try:
                student.photo = request.FILES.get('photo')
                student.phone = request.POST.get('phone')
                student.twitter = request.POST.get('twitter')
                student.facebook = request.POST.get('facebook')
                student.instagram = request.POST.get('instagram')
                student.about = request.POST.get('about')
                student.save()
            except:
                messages.error(request, "Invalid details")
            messages.success(request, "Your profile is updated successfully")
            redirect('/me/profile')

        return render(request, 'dashboard/profile.html', {'student': student})
    else:
        return redirect('/')


def view_book(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        books = Book.objects.raw(
            "select * from dashboard_book as d inner join (SELECT bookid_id,group_concat(author) " +
            " as auth from dashboard_author GROUP by bookid_id) as e on d.bookid = e.bookid_id " +
            "inner join (SELECT bookid_id ,count(copy_no) as cou from dashboard_copy  where status = 'Available' " +
            "group by bookid_id) as a on d.bookid = a.bookid_id ;")

        json_books = {}
        for book in books:
            json_books[book.bookid] = {
                'bookid': book.bookid,
                'picture': str(book.picture),
                'title': book.title,
                'auth': book.auth,
                'publication': book.publication,
                'isbn': book.isbn,
                'cou': book.cou,
                'desc': book.desc,
            }
        books_json = json.dumps(json_books)
        # print(books_json)
        return render(request, 'dashboard/view.html', {'student': student, 'books': books, 'books_json': books_json})
    else:
        return redirect('/')


def add_book(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_admin:
            if request.method == "POST" and 'addbookwithforms' in request.POST:
                bookid = request.POST['bookid']
                name = request.POST['name']
                price = request.POST['price']
                publication = request.POST['publication']
                author = request.POST['author']
                isbn = request.POST['isbn']
                desc = request.POST['description']
                copies = request.POST['copies']
                picture = request.FILES['picture']

                book = Book(bookid=bookid, title=name, price=price, desc=desc, publication=publication, isbn=isbn,
                            picture=picture)
                book.save()

                for i in range(1, int(copies) + 1):
                    copy = Copy(bookid=book, copy_no=i)
                    copy.save()

                author = author.split(',')
                for i in author:
                    aut = Author(bookid=book, author=i)
                    aut.save()

            if request.method == "POST" and 'addbookwithcsv' in request.POST:
                csvfile = request.FILES['csvfile']
                print(".................", csvfile)
                file_data = csvfile.read().decode("utf-8")
                lines = file_data.split("\n")
                for line in lines:
                    fields = line.split(",")

                    bookid = fields[0]
                    title = fields[1]
                    price = int(fields[2])

                    publication = fields[3]
                    author = fields[4]
                    isbn = fields[5]
                    desc = fields[6]
                    numofcopies = int(fields[7])

                    book = Book(bookid=bookid, title=title, price=price, desc=desc, publication=publication, isbn=isbn,
                                picture='books/bookimage.jpg')
                    book.save()

                    for i in range(1, numofcopies + 1):
                        copy = Copy(bookid=book, copy_no=i)
                        copy.save()

                    author = author.split(',')
                    for i in author:
                        aut = Author(bookid=book, author=i)
                        aut.save()

            return render(request, 'dashboard/add_book.html', {'student': student})

    return redirect('/')


def view_damage_report(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_admin:
            damage = Damage.objects.all()
            return render(request, 'dashboard/view_damage_report.html', {'student': student, 'damage': damage})
        else:
            return redirect('/me')

    else:
        return redirect('/me')


def report_damage(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if request.method == "POST":
            try:
                roll_no = request.POST['roll_no']
                book_id = request.POST['book_id']
                copy_no = request.POST['copy_no']
                desc = request.POST['desc']
                try:
                    iss = Issue.objects.get(
                        bookid=book_id, roll_no=roll_no, copy_no=copy_no, date_returned=None)
                    try:
                        book = Book.objects.get(bookid=book_id)
                        d = Damage.objects.create(
                            bookid=book, roll_no=roll_no, copy_no=copy_no, damage_desc=desc)
                        d.save()
                        messages.success(
                            request, "Your Damage report has been updated successfully")
                    except Book.DoesNotExist:
                        messages.error(
                            request, "Please enter a valid book number")

                except Issue.DoesNotExist:
                    messages.error(request, "You haven't issued the book")

            except:
                messages.error(request, "Invalid details")
        return render(request, 'dashboard/report_damage.html', {'student': student})
    else:
        return redirect('/me')


# def send_email(request):
#     send_mail(request)
#     return redirect('/me/view-damage')

def send_mail(request):
    print("in views....send_mail")
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_admin:
            if request.method == "POST" and 'damage' in request.POST:
                book_id = request.POST.get('book_id')
                copy_no = request.POST.get('copy_no')
                roll_no = request.POST.get('roll_no')
                email = Student.objects.get(roll_no=roll_no)
                email = email.mail
                print(book_id, copy_no, roll_no, email, sep="\n")
                return render(request, 'dashboard/send_mail.html', {'student': student, 'book_id': book_id,
                                                                    'copy_no': copy_no, 'roll_no': roll_no,
                                                                    'email': email})
            elif request.method == "POST" and 'mail' in request.POST:
                mail = request.POST.get('email')
                subject = request.POST.get('subject')
                body = request.POST.get('body')
                send_email.delay(request, subject, body, mail)

                return redirect('/me/view-damage')
            else:
                return redirect('/me/view-damage')

        else:
            return redirect('/me')

    else:
        return redirect('/me')


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


def error404(request, exception):
    return render(request, 'dashboard/404.html')
