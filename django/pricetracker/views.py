from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from .models import  Product, User
from background_task import background
#---------------------------------------------
from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import html   

#---------------------------------------------
@background(schedule = 10)
def get_price(product_id):
    p = Product.objects.get(pk = product_id)
    s = BeautifulSoup(urlopen(link), features="lxml")
    title = p.site_title
    if title == "Amazon":
        try:
            Price = s.find()
        except:
            try:
                Price =
            except:
                Price = 
        temp = ""
        for i in Price:
            if i.isdigit() or i == ".":
                temp = temp+i
        price = float(temp)
        p.update(last_checked_price=price)

#---------------------------------------------
def homeView(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
    #----------------------------------------------------
        if request.method == 'POST':
            link = request.POST.get('link')
            des_price = request.POST.get('des_price')
            s = BeautifulSoup(urlopen(link), features="lxml")
            title = s.title.get_text()
            product_title = s.find("span",attrs = {'id':'productTitle'}).text
            if "Amazon.in" in title:
                title = "Amazon"
            elif "Flipkart.com" in title:
                title = "Flipkart"
            elif "eBay" in title:
                title = "eBay"
            else:
                return HttpResponse("We currently don't support this website.")
            
    #----------------------------------------------------
            u = User.objects.get(username=current_user)
            p = u.product_set.create(link=link, desired_price=des_price, site_title = title, product = product_title)
            get_price(p.id)

            return render(request, 'pricetracker/home.html', param)
        else:
            return render(request,'pricetracker/home.html', param )        
    else:
        return redirect( 'login')
    return redirect(request,'pricetracker/login.html')

def signupView(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print("hi")
        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, emailaddress=email, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'pricetracker/signup.html')

def loginView(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username = uname, password= pwd)

        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')
    
    return render(request, 'pricetracker/login.html')

    
def logoutView(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


   
    
    
    



    
