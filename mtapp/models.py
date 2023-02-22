from django.db import models
from django.contrib.auth.models import User



# Create your models here.
# class regmodel(models.Model):
#     username=models.CharField(max_length=30)
#     email=models.EmailField(max_length=30)
#     phone=models.IntegerField()
#     address=models.CharField(max_length=30)
#     pincode=models.IntegerField()
#     password=models.CharField(max_length=30)

class mermodel(models.Model):
    Outlet=models.CharField(max_length=30)
    Outlet_Location=models.CharField(max_length=60)
    Outlet_Id=models.IntegerField()
    Email_address=models.EmailField(max_length=50)
    Mobile_Number=models.IntegerField()
    Password=models.CharField(max_length=30)
    def __str__(self):
        return self.Outlet

class proupmodel(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='mtapp/static/images')

    def __str__(self):
        return self.product_name

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user



#we have a user model
#username,email,first name,last name,password


class cart(models.Model):
    product_image = models.ImageField()
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField()
    def __str__(self):
        return self.product_price


class wishlist(models.Model):
    product_image = models.ImageField()
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_price


class buy(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.quantity,self.product_price

class card_model(models.Model):
    card_holder_name = models.CharField(max_length=50)
    card_number = models.IntegerField()
    date = models.CharField(max_length=60)
    security_code = models.IntegerField()

    def __str__(self):
        return self.card_holder_name










