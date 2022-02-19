from django.shortcuts import render, redirect
from django.contrib.auth import logout
from home.models import Student
from .models import *


# Create your views here.
def dashboard(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_admin:
            return render(request, 'dashboard/ad_dashboard.html', {'student': student})
        else:
            return render(request, 'dashboard/dashboard.html', {'student': student})
    else:
        return redirect('/')


def log_out(request):
    logout(request)
    return redirect('/')


def renew(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        return render(request, 'dashboard/renew.html', {'student': student})
    else:
        return redirect('/')


def profile(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if request.method == 'POST':
            student.photo = request.FILES.get('photo')
            student.phone = request.POST.get('phone')
            student.twitter = request.POST.get('twitter')
            student.facebook = request.POST.get('facebook')
            student.instagram = request.POST.get('instagram')
            student.about = request.POST.get('about')
            student.save()
            redirect('/me/profile')

        return render(request, 'dashboard/profile.html', {'student': student})
    else:
        return redirect('/')


def view_book(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        books = Book.objects.all()
        return render(request, 'dashboard/view.html', {'student': student, 'books': books})
    else:
        return redirect('/')


def add_book(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_admin:
            if request.method == "POST":
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

            return render(request, 'dashboard/add_book.html', {'student': student})

    return redirect('/')


def view_damage_report(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_admin:
            return render(request, 'dashboard/view_damage_report.html', {'student': student})
        else:
            return redirect('/me')

    else:
        return redirect('/me')


def report_damage(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        return render(request, 'dashboard/report_damage.html', {'student':student})
    else:
        return redirect('/me')

def error404(request, exception):
    return render(request, 'dashboard/404.html')
