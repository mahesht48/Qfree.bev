from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from nthproject.settings import EMAIL_HOST_USER
import datetime
from datetime import timedelta

import django.shortcuts


# Create your views here.
def index(request):
    return render(request, 'index.html')


# def reg(request):
#     if request.method=='POST':
#         a=regform(request.POST)
#         if a.is_valid():
#             un=a.cleaned_data["user_name"]
#             el=a.cleaned_data["last_name"]
#             ph=a.cleaned_data["first_name"]
#             add=a.cleaned_data['email_address']
#             pi=a.cleaned_data['pincode']
#             pad=a.cleaned_data['password']
#             cpd=a.cleaned_data["confirmpassword"]
#             if pad==cpd:
#                b=regmodel(user_name=un,email=el,phone=ph,address=add,pincode=pi,password=pad)
#                b.save()
#                return HttpResponse("process accomplished")
#         else:
#
#             return HttpResponse("registration unsuccessful")
#     return render(request,'registration.html')

# def log(request):
#     if request.method=='POST':
#         a=logform(request.POST)
#         if a.is_valid():
#             un=a.cleaned_data["user_name"]
#             pad=a.cleaned_data["password"]
#             b=regmodel.objects.all()
#             for i in b:
#                 if un == i.user_name and pad == i.password:
#                     return HttpResponse("user found")
#             else:
#                 return HttpResponse("user not found")
#     return render(request,'login.html')
def mer(request):
    if request.method == 'POST':
        a = merform(request.POST)
        if a.is_valid():
            ot = a.cleaned_data["Outlet"]
            ol = a.cleaned_data["Outlet_Location"]
            oi = a.cleaned_data["Outlet_Id"]
            ea = a.cleaned_data["Email_address"]
            mn = a.cleaned_data["Mobile_Number"]
            ps = a.cleaned_data["Password"]
            cp = a.cleaned_data["Confirm_Password"]
            if ps == cp:
                b = mermodel(Outlet=ot, Outlet_Location=ol, Outlet_Id=oi, Email_address=ea, Mobile_Number=mn,
                             Password=ps)
                b.save()
                return redirect(mlog)
            else:
                return HttpResponse("registration failed")
        else:
            return HttpResponse('')
    return render(request, 'merchant reg.html')


def mlog(request):
    if request.method == 'POST':
        a = mlogform(request.POST)
        if a.is_valid():
            ot = a.cleaned_data["Outlet_Id"]
            ps = a.cleaned_data["Password"]
            # to make a variable global
            request.session['Out_Id'] = ot

            b = mermodel.objects.all()
            for i in b:
                if ot == i.Outlet_Id and ps == i.Password:
                    return redirect(pro)
            else:
                return HttpResponse("user not found")
    return render(request, 'merchant log.html')


def pro(request):
    Outlet_Id = request.session['Out_Id']
    return render(request, 'profile.html', {'Outlet_Id': Outlet_Id})


def proup(request):
    if request.method == 'POST':
        a = proupform(request.POST, request.FILES)
        if a.is_valid():
            pn = a.cleaned_data["product_name"]
            pp = a.cleaned_data["product_price"]
            pi = a.cleaned_data["product_image"]
            b = proupmodel(product_name=pn, product_price=pp, product_image=pi)
            b.save()
            return HttpResponse("product added")
        else:
            return HttpResponse("mission unsuccessful")
    return render(request, 'product upload.html')


def prodis(request):
    a = proupmodel.objects.all()
    product = []
    price = []
    name = []
    id = []
    for i in a:
        id2 = i.id
        id.append(id2)

        pi = i.product_image
        product.append(str(pi).split('/')[-1])
        pp = i.product_price
        price.append(pp)
        pn = i.product_name
        name.append(pn)
    mylist = zip(product, price, name, id)
    return render(request, 'productdisplay.html', {'mylist': mylist})


# models.objects.get(id=id)
def productdelete(request, id):
    a = proupmodel.objects.get(id=id)
    a.delete()
    return redirect(prodis)


def editproduct(request, id):
    a = proupmodel.objects.get(id=id)
    im = str(a.product_image).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES):
            if len(a.product_image) > 0:  # old file checking
                os.remove(a.product_image.path)
            a.product_image = request.FILES['product_image']
        a.name = request.POST.get('product_name')
        a.price = request.POST.get('product_price')
        a.save()
        return redirect(prodis)
    return render(request, 'editproduct.html', {'a': a, 'im': im})


def regis(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        ema = request.POST.get('email')
        lna = request.POST.get('last_name')
        fna = request.POST.get('first_name')
        password = request.POST.get('password')

        # checking whether the username exist,to change error in user import
        if User.objects.filter(
                username=uname).first():  ###user_name::::filter method is used to filter ur search and allows u to return only the row that matches the search top
            # first fun:::it will get first object from filter query...

            messages.success(request,
                             'username already')  # message.succes is a frame work tha allows u to store messages in one request and retrieve them in the request page
            return redirect(regis)
        user_obj = User(username=uname, email=ema, first_name=fna, last_name=lna)
        user_obj.set_password(password)
        user_obj.save()

        # uuid module=universally unique identifiers
        # import uuid
        auth_token = str(uuid.uuid4())
        profile_obj = profile.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        # user defined
        send_mail_regis(ema, auth_token)  # mail sending function,user defined function

        return render(request, 'success.html')
    return render(request, 'registration.html')


def send_mail_regis(email, auth_token):
    subject = "your account has been verified"
    message = f'click the link to verify your account http://127.0.0.1:8000/verify/{auth_token}'
    email_from = EMAIL_HOST_USER  # get email from.
    recipient = [email]  ## to..always add email of a recepient in list.
    ## inbuild function
    send_mail(subject, message, email_from, recipient)  # import send_mail


# f=formatter;It is a string literal which contains expressions inside curly brackets.The expressions are replaced by values


# def userprofile(request):
#     return render(request,'userprofile.html')

def verify(request, auth_token):
    profile_obj = profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:  # if profile_object false
            messages.success(request, 'your account is already verified')
            return redirect(login)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'your account has been verified')
        return redirect(login)
    else:
        messages.success(request, "user n ot found")
        return redirect(login)


def login(request):
    if request.method == 'POST':
        urna = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=urna).first()
        # user_obj=anshya
        # user_obj=shan
        if user_obj is None:  # if user doesnt exist
            messages.success(request, 'user not found')
            return redirect(login)
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:  # if not profile is verified

            messages.success(request, 'profile not verified check your email')
            return redirect(login)
        user = authenticate(username=urna, password=password)
        # user=valid
        # if the given credentials are valid, return aUser object.
        if user is None:
            messages.success(request, 'wrong password or username')
            return redirect(login)
        return redirect(userprofile)
    return render(request, 'login.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def dis_all_products(request):
    a = proupmodel.objects.all()
    product = []
    price = []
    name = []
    id = []

    for i in a:
        id2 = i.id
        id.append(id2)

        pi = i.product_image
        product.append(str(pi).split('/')[-1])
        pp = i.product_price
        price.append(pp)
        pn = i.product_name
        name.append(pn)
    mylist = zip(product, price, name, id)
    return render(request, 'displayproduct.html', {'mylist': mylist})


def addcart(request, id):
    t = proupmodel.objects.get(id=id)
    u = cart(product_image=t.product_image, product_name=t.product_name, product_price=t.product_price, )
    u.save()
    return redirect(cartdisplay)


def wishlist1(request, id):
    j = proupmodel.objects.get(id=id)
    l = wishlist(product_image=j.product_image, product_name=j.product_name, product_price=j.product_price, )
    l.save()
    return redirect(wishlistdisplay)


def wishlistdisplay(request):
    c = wishlist.objects.all()
    product = []
    price = []
    name = []
    id = []

    for i in c:
        id3 = i.id
        id.append(id3)
        pi = i.product_image
        product.append(str(pi).split('/')[-1])
        pp = i.product_price
        price.append(pp)
        pn = i.product_name
        name.append(pn)
    mylist = zip(product, price, name, id)
    print(id)
    return render(request, 'wishlist.html', {'mylist': mylist})


def cartdisplay(request):
    d = cart.objects.all()
    product = []
    price = []
    name = []
    id = []

    for i in d:
        id4 = i.id
        id.append(id4)
        pi = i.product_image
        product.append(str(pi).split('/')[-1])
        pp = i.product_price
        price.append(pp)
        pn = i.product_name
        name.append(pn)
    mylist = zip(product, price, name, id)
    return render(request, 'cart.html', {'mylist': mylist})


def delete_wish(request, id):
    d = wishlist.objects.get(id=id)
    d.delete()
    return redirect(wishlistdisplay)


def delete_cart(request, id):
    h = cart.objects.get(id=id)
    h.delete()
    return redirect(cartdisplay)


def buyme(request, id):
    w = cart.objects.get(id=id)
    im = str(w.product_image).split('/')[-1]
    if request.method == 'POST':
        name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        b = buy(product_name=name, quantity=quantity, product_price=price)
        b.save()
        total = int(price) * int(quantity)
        return render(request, 'finalbill.html', {'total': total, 'name': name, 'quantity': quantity, 'price': price})
    return render(request, 'buythis.html', {'w': w, 'im': im})


def customerdet(request):
    if request.method == 'POST':
        card_holder_name = request.POST.get('card_holder_name')
        card_number = request.POST.get('card_number')
        date = request.POST.get('date')
        security_code = request.POST.get('security_code')
        user_obj = card_model(card_holder_name=card_holder_name, card_number=card_number, date=date,
                              security_code=security_code)
        user_obj.save()
        today = datetime.date.today()
        today += timedelta(days=10)
        return render(request, "succ.html", {'date': today})

    return render(request, 'finalbill.html')


def succ(request):
    return render(request, 'customerdetails.html')


def ordersummary(request):
    return render(request, 'succ.html')
