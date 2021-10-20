from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contacts
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable1":"om is a good person",
        "variable2":"sanu is a good person"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contacts(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your massage has been sent')

    return render(request, 'Contact.html')
    #return HttpResponse("this is contact page")


def about(request):
    return render(request, 'About.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'Services.html')
    #return HttpResponse("this is services page")




