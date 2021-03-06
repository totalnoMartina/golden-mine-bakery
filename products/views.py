from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ Rendering all products """
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)

def product_info(request, product_id):
    """ Rendering detailed information on the product """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_infos.html', context)
