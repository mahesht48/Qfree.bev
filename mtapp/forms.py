from django import forms

class regform(forms.Form):
    user_name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=30)
    phone=forms.IntegerField()
    address=forms.CharField(max_length=30)
    pincode=forms.IntegerField()
    password=forms.CharField(max_length=30)
    confirmpassword=forms.CharField(max_length=30)

class logform(forms.Form):
    OU=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class merform(forms.Form):
    Outlet=forms.CharField(max_length=30)
    Outlet_Location=forms.CharField(max_length=60)
    Outlet_Id=forms.IntegerField()
    Email_address=forms.EmailField(max_length=50)
    Mobile_Number=forms.IntegerField()
    Password=forms.CharField(max_length=30)
    Confirm_Password=forms.CharField(max_length=30)

class mlogform(forms.Form):
    Outlet_Id=forms.IntegerField()
    Password=forms.CharField(max_length=30)
class proupform(forms.Form):
    product_name=forms.CharField(max_length=30)
    product_price=forms.IntegerField()
    product_image=forms.FileField()


class customerdetails(forms.Form):
    card_holder_name= forms.CharField(max_length=30)
    card_number= forms.IntegerField()
    date = forms.DateTimeField()
    security_code=forms.CharField(max_length=50)
