from django.shortcuts import render,redirect
from app1.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"sign-up.html")

def dashboard(request):
    product_obj = Product.objects.all()
    return render(request,'dashboard.html',{'product_obj':product_obj})

def ragistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        shoop_name = request.POST['shoop_name']
        password = make_password(request.POST['password'])
        if Shopkiper.objects.filter(email=email).exists():
            return HttpResponse("Email Already Exists")
        elif Shopkiper.objects.filter(mobile=mobile).exists():
            return HttpResponse("Mobile Number Already Exists")
        elif Shopkiper.objects.filter(password= password).exists():
            return HttpResponse("Password Already Exists")
        else:
            Shopkiper.objects.create(name=name,email=email,
                mobile=mobile,shoop_name=shoop_name,password=password)
            return redirect(request,"/signup/")
    
def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_pwd = request.POST['password']
        if Shopkiper.objects.filter(email=email).exists():
            obj = Shopkiper.objects.get(email=email)
            password = obj.password
            if check_password(user_pwd,password):
                return redirect("/dashboard/")
            else:
                return HttpResponse('Password Encorect')
        else:
            return HttpResponse("Email Not Ragistrate")
        

def product(request):
    if request.method == 'POST':
        title = request.POST['title']
        discribe = request.POST['discribe']
        pro_img = request.FILES['pro_img']
        Product.objects.create(title=title,pro_img=pro_img,discription=discribe)
        return redirect('/dashboard/')
         
def updateuser(request,uid):
    data = Product.objects.get(id=uid)
    return render(request,'update.html',{'data':data})

def delete(request,qk):
    Product.objects.get(id=qk).delete()
    return redirect('/dashboard/')


def view_update(request):
    if request.method == 'POST':
        form_data = request.POST
        title = form_data['title']
        discription = form_data['discription']
        pro_img = form_data['pro_img']
        Product.objects.create(title=title,discription=discription,pro_img=pro_img)
        data = Product.objects.all()
        return redirect('/dashboard/')
