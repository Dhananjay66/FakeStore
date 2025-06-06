# store/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from .fetch_api_data import fetch_and_store_products
from django.db.models import Q

def product_list(request):
    fetch_and_store_products()
    query = request.GET.get('q')
    category = request.GET.get('category')
    
    products = Product.objects.all()

    if query:
        products = products.filter(title__icontains=query)

    if category and category != 'all':
        products = products.filter(category__iexact=category)

    categories = Product.objects.values_list('category', flat=True).distinct()

    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
    })
