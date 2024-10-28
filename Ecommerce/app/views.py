from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import send_email_to_client
from django.http import Http404
import os
from .models import Phone,Orders,Device
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    phones = Phone.objects.all()
    if request.GET.get('search'):
        phones = Phone.objects.filter(name__icontains=request.GET.get('search'))
    
        
    paginator = Paginator(phones, 25)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    

    return render(request, 'index.html',{'page_obj': page_obj})

def register(request):
    if request.method =='POST':

        first_name=request.POST['firstname']    
        last_name=request.POST['lastname']    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():   
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,password=password, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('login')
    else:  
        return render(request, 'register.html')
        
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if request.POST.get('forgotpassword'):
            return redirect('changepassword')
        
        user = auth.authenticate(username=username,password=password)

        if user is not None: 
            auth.login(request, user)
            return redirect('/') 
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    return render(request, 'login.html')
            
def logout(request):
    auth.logout(request)
    return redirect('/')

def changepassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        

        if User.objects.filter(email=email).exists():
            with open('email.txt', 'w') as file:
                file.write(email)
            gen_code = send_email_to_client(email)
            with open('code.txt', 'w') as file:
                file.write(str(gen_code))
            
                return redirect('setpassword')
        else:
            messages.info(request, 'Email does not exist')
            return redirect('changepassword')
    return render(request,'changepass.html')

def setpassword(request):
    if request.method == 'POST':

        code = request.POST.get('code')

        with open('code.txt','r') as file:
            get_code = file.read()

        if code == get_code:
            if os.path.exists('code.txt'):
                os.remove('code.txt')
            return redirect('newpassword')
        
        else:
            messages.info(request,'Incorrect Code')
            return redirect('setpassword')
    return render(request,'setpassword.html')

def newpassword(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            with open('email.txt','r') as file:
                email = file.read()
                user = User.objects.get(email=email)
                user.set_password(password1)
                user.save()
            os.remove('email.txt')
            messages.success(request,"Password has been changed")
            return redirect('index')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('newpassword')

    return render(request,'newpassword.html')

@login_required(login_url='login')
def cart(request,id):
    try:
        phone = Phone.objects.get(id=id)  # This retrieves the Phone instance
    except Phone.DoesNotExist:
        raise Http404("Phone not found.")
    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        number = request.POST.get('phone')
        Orders.objects.create(
            phone_id=phone,
            customer_id = request.user,
            customer_address = address,
            customer_city = city,
            customer_zip_code = zip,      
            customer_phone = number               
)
        return redirect('confirm')

    return render(request, 'cart.html',{'phone':phone})

def confirm(request):
    customer = Orders.objects.filter(customer_id=request.user.id).order_by('-order_date')[0]
    if request.method == 'POST':
        if request.POST.get('confirm'):
            return redirect('thanks')
        if request.POST.get('cancel'):
            customer.delete()
            return redirect('index')
        
    return render(request, 'confirm.html',{'customer':customer})

def details(request,name):
    try:
        info = Device.objects.filter(model = name)[0]
        return render(request, 'details.html',{'info':info})
    except:
        info = Phone.objects.filter(name = name)[0]
        return render(request, 'details404.html',{'info':info})
    

def thanks(request):
    
    return render(request, 'thanks.html')