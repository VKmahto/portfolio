from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
import datetime


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file_path = r'C:\Users\Welcome\Desktop\inquiries.txt'
        with open(file_path, 'a') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Message: {msg}\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write('-' * 40 + '\n')

        messages.success(request, 'Details Added Successfully')
        return redirect('index')
    return render(request, 'index.html')


