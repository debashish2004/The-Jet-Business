from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is home page")

def about(request):
    return render(request,"about.html")
    #return HttpResponse("This is about page")

def services(request):
    return render(request,"services.html")
    #return HttpResponse("This is services page")
def contact(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        jet = request.POST.get('jet')
        budget = request.POST.get('budget')
        contact = Contact(f_name=f_name,l_name=l_name,email=email,phone=phone,jet=jet,budget=budget,date=datetime.today())
        contact.save()
        messages.success(request,"Form has been submitted successfully!")
        
    return render(request,"contact.html")

def static(request):
    return render(request,"index.html")
    #return HttpResponse(static.test)
def jets(request):
    return render(request,"jets.html")
def gallery(request):
    return render(request,"gallery.html")