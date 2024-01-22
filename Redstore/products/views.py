from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request, 'index.html')

def products_list(request):
    page_request=1
    if request.GET:
        page_request=request.GET.get('page_request',1)
    product_list_data=Products.objects.all()
    product_paginator = Paginator(product_list_data, 4)
    product_list_data=product_paginator.get_page(page_request)
    product_list_data={
        'product_list_data':product_list_data
    }
    return render(request, 'products.html',product_list_data)

def products_details(request):
    return render(request, 'products_details.html')

