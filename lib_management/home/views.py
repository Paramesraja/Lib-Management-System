from django.shortcuts import render, redirect
from django.http import HttpResponse
import razorpay
from razorpay.utility.utility import SignatureVerificationError
from django.views.decorators.csrf import csrf_exempt
from .models import Donate
import datetime
import json


client = razorpay.Client(auth=("rzp_test_u7deuTCyVkMz9G", "R1GpzfJTzkDwVJpt2O0kHdsI"))


def home(request):
    if request.session.get('roll_no'):
        return redirect('/me')
    else:
        return render(request, 'home/home.html')


def donate(request):
    return render(request, 'home/donate.html', )


def payment(request):
    if request.method == "POST":
        d_name = request.POST.get('d_name')
        d_email = request.POST.get('d_email')
        d_phone = request.POST.get('d_phone')
        d_amount = request.POST.get('d_amount')
        data = {"amount": int(d_amount) * 100, "currency": "INR", "payment_capture": "1"}
        d_payment = client.order.create(data=data)
        order_id = d_payment['id']
        donate = Donate(name=d_name, email=d_email, phone=d_phone, amount=d_amount, razorpay_order_id=order_id)
        donate.save()
        return render(request, 'home/donate_summary.html', {'d_name': d_name, 'd_email': d_email,
                                                            'd_phone': d_phone, 'd_amount': d_amount,
                                                            'order_id': order_id})

    else:
        return redirect('/donate')


@csrf_exempt
def success(request):
    if request.method == "POST":

        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        print(razorpay_signature,razorpay_order_id,razorpay_payment_id)
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }
        try:
            result = client.utility.verify_payment_signature(params_dict)
            donate = Donate.objects.get(razorpay_order_id=razorpay_order_id)
            donate.razorpay_signature = razorpay_signature
            donate.razorpay_payment_id = razorpay_payment_id
            donate.date_donated = datetime.datetime.now()
            if result == None:
                donate.status = 1
                donate.save()
                return render(request, 'home/success.html')
            else:
                donate.status = 0
                donate.save()
                return render(request, 'home/sorry.html')
        except SignatureVerificationError:
            razorpay_order = request.POST.get('error[metadata]')
            razorpay_order = json.loads(razorpay_order)
            razorpay_order_id = razorpay_order['order_id']
            donate = Donate.objects.get(razorpay_order_id=razorpay_order_id)
            donate.razorpay_payment_id = razorpay_order['payment_id']
            donate.date_donated = datetime.datetime.now()
            donate.status = 0
            donate.save()
            return render(request, 'home/sorry.html')
    else:
        redirect('/donate')


def check(request):
    return render(request, 'home/success.html')
