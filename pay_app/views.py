
from django.http import HttpRequest, HttpResponse 
from django.shortcuts import get_object_or_404, redirect, render
from .form import PaymentForm
from django.conf import settings
from django.contrib import messages
from . models import Payment


# Create your views here.

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            pay = form.save()
            return render(request, 'payment.html', {'pay': pay, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        form = PaymentForm()
    return render(request, 'initiate_pay.html', {'form':form})


def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.error(request, 'Verification Failed')
    else:
        
        messages.success(request, 'Verification Successful')
    return redirect('pay_app:initiate-payment')
