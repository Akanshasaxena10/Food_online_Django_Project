from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from .forms import UserForm
from .models import User,UserProfile
from django.contrib import messages
from vendor.forms import VendorForm

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        
        print(request.POST) 
        form = UserForm(request.POST)
        if form.is_valid():
            ##create user using the form
            #  password =form.cleaned_data['password']
            #  user = form.save(commit=False)###to assign the role we are leaving an opportunity to make modifications
            #  user.set_password(password)
            #  user.role =user.CUSTOMER
            #  user.save()
            
            #create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            print("user is saved")
            messages.success(request, "Your account has been registered successfully.")
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)
    else:   
       form = UserForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/registerUser.html', context)

def registerVendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid:
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request,"Your account has been registered successfully! Please wait for the approval.")
            return redirect('registerVendor')
        else:
            print("Invalid Form")
            print(form.errors)
       ###store and save the data and create user
    else:   
        form = UserForm()##we need to add user and vendor form to register the vendor
        v_form = VendorForm()
    context = {
        'form' : form,
        'v_form' : v_form,
    }
    return render(request, 'accounts/registerVendor.html',context)