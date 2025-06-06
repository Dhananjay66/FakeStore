import requests
from .models import Product

def fetch_and_store_products():
    if Product.objects.exists():
        return  # Don't fetch again if data already exists

    response = requests.get('https://fakestoreapi.com/products')
    data = response.json()

    for item in data:
        Product.objects.create(
            title=item['title'],
            price=item['price'],
            description=item['description'],
            category=item['category'],
            image=item['image'],
            rating_rate=item['rating']['rate'],
            rating_count=item['rating']['count']
        )