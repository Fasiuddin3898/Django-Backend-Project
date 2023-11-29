from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages

def home(request):
    messages.success(request,"Welcome to arka")
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contacts(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        planning_which_country = request.POST.get('planning_which_country')
        qualification = request.POST.get('qualification')
        tell_about_yourself = request.POST.get('tell_about_yourself')
        
        # Creating a Contact object and saving it to the database
        contact = Contact(
            full_name=full_name,
            city=city,
            phone_number=phone_number,
            email_address=email_address,
            planning_which_country=planning_which_country,
            qualification=qualification,
            tell_about_yourself=tell_about_yourself
        )
        contact.save()
        messages.success(request, "Yor details has been saved our executive will contact you...!")
          # You might want to redirect to a success page
        
    return render(request, "contacts.html")
