from django.shortcuts import render, redirect
from .form import account
from django.contrib.auth import authenticate, login
import random
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def custom_form(request):
    if request.method == 'POST':
        form = account(request.POST)

        if form.is_valid():
            form.save()   
            

    else:
        form = account()
    return render(request, 'main.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('verfication_login_code') # Redirect to a success page.
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def verfication_login_code(request):
    Code=random.randint(1000,9999)
    if request.method == 'POST':
         input_code=request.POST.get('code')
         if str(Code)==input_code:
            email_body = render_to_string("Verification.html",{'code': Code,})
            email_message = EmailMessage(
            'Verification Code',
            email_body,
            settings.EMAIL_HOST_USER,
            [Code]
        )
            return redirect('Home')
         else:
                return render(request, 'verfication_login_code.html', {'error': 'Invalid code. Please try again.'})
    return render(request, 'verfication_login_code.html')
