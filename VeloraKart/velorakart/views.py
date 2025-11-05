from store.models import Product
from django.shortcuts import render

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')[:10]

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'company/about.html')

def careers(request):
    return render(request, 'company/careers.html')

def terms(request):
    return render(request, 'company/terms.html')

def contact(request):
    return render(request, 'support/contact.html')

def refund(request):
    return render(request, 'support/refund.html')

def order_status(request):
    return render(request, 'support/order_status.html')

def shipping_info(request):
    return render(request, 'support/shipping_info.html')

def dispute(request):
    return render(request, 'support/dispute.html')

