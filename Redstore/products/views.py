from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products=Products.objects.order_by('priority')[:4]
    latest_products=Products.objects.order_by('-id')[:4]
    products={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request, 'index.html',products)

def products_list(request):
    page_request=1
    if request.GET:
        page_request=request.GET.get('page_request',1)
    product_list_data=Products.objects.order_by('priority')
    product_paginator = Paginator(product_list_data, 4)
    product_list_data=product_paginator.get_page(page_request)
    product_list_data={
        'product_list_data':product_list_data
    }
    return render(request, 'products.html',product_list_data)

def products_details(request,pk):    #pk means primary key
    products=Products.objects.get(pk=pk)
    products_dict={
        'product':products
    }
    return render(request, 'products_details.html',products_dict)

