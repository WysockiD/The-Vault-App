from django.shortcuts import render, redirect

from .models import Product, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {
        'products': products
    })


def product_details(request, product_slug):
    try:
        selected_product = Product.objects.get(slug=product_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_product.participants.add(participant)
                return redirect('confirm-registration', product_slug=product_slug)

        return render(request, 'products/product-details.html', {
                'product_found': True,
                'product': selected_product,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'products/product-details.html', {
            'product_found': False
        })


def confirm_registration(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, 'products/registration-success.html', {
        'organizer_email': product.organizer_email
    })