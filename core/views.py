from django.shortcuts import render
from .models import *

from django.contrib import messages
from django.shortcuts import render, redirect
def home(request):
    hero_section = HeroSection.objects.first()  
    about_home = AboutHomePage.objects.first()
    products_list = ProductHomePage.objects.all()  
    statistics = Statistic.objects.all()
    project_home_page = ProjectHomePage.objects.all()
    partners = Partners.objects.all()
    context = {
        'about_home': about_home,
        'hero_section': hero_section,
        'products': products_list,  
        'statistics': statistics,
        'projects': project_home_page,
        'partners':partners,
    }
    return render(request, "index.html", context)




def about(request):
    about_info = AboutUs.objects.first()  
    certificate=Certificate.objects.all()
    context = {
        'about_info': about_info,
        'certificate': certificate
    }
    return render(request, 'about.html', context)


def contact(request):
    success_message = ""  # Mesajın göndərilib-göndərilmədiyini bildirmək üçün dəyişkən

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        success_message = "Mesajınız göndərildi."
        return render(request, 'contact.html', {'success_message': success_message})

    return render(request, 'contact.html', {'success_message': success_message})