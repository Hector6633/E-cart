from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def products_list(request):
    return render(request, 'products.html')

def products_details(request):
    return render(request, 'products_details.html')

