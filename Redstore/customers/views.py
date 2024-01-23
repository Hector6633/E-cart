from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Customers
from django.contrib import messages

# Create your views here.
def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        
        try:
            username=request.POST['username']
            email=request.POST['email']
            phone_number=request.POST['phonenumber']
            password=request.POST['password']
            # create user account.
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            # create customer account.
            customer=Customers.objects.create(
                user=user,
                phone_number=phone_number
            )
            success_message='User Registered Successfully'
            messages.success(request,success_message)
        except Exception as e:
            error_message='User Registered Successfully'
            messages.error(request, error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False     
        username=request.POST['username']
        password=request.POST['password']  
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Invalid Creaditials')
    return render(request, 'account.html')

def sign_out(request):
    logout(request)
    return redirect('index')