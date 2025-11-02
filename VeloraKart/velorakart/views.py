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
