from django.shortcuts import render, redirect
from django.contrib.auth import logout
from home.models import Student


# Create your views here.
def dashboard(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        return render(request, 'dashboard/layout.html', {'student': student})
    else:
        return redirect('/')


def log_out(request):
    logout(request)
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


def error404(request, exception):
    return render(request, 'dashboard/404.html')
