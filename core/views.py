from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import  Product,ContactMessage


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address.")
            return render(request, "contact.html")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")

    messages_list = ContactMessage.objects.all()

    return render(request, "contact.html", {"messages": messages_list})

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})