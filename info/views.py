from django.shortcuts import render,HttpResponse,redirect
from list.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Send an email notification
        subject = 'New Contact Form Submission'
        message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['dhruvilantala123@gmail.com']  # Replace with your email address

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request, "Your data has been send successfully!! I will respond within 24 hours.")
    return render(request, "index.html")



