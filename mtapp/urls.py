from django.urls import path
from .views import *

urlpatterns=[

    path('',index),
    path('registration/',regis),
    path('login/',login),
    path('merchantreg/',mer),
    path('merchantlog/',mlog),
    path('pro/',pro),
    path('proup/',proup),
    path('prodis/',prodis),
    path('delete/<int:id>',productdelete),
    # delete/7
    path('edit/<int:id>',editproduct),
    path('verify/<auth_token>',verify),
    path('userprofile/',userprofile),
    path('dis_all_products/',dis_all_products),
    path('proview/',dis_all_products),
    path('wishlist/<int:id>/',wishlist1),
    path('cart/<int:id>/',addcart),
    path('wishlist/',wishlistdisplay),
    path('cart/',cartdisplay),
    path('delwish/<int:id>/',delete_wish),
    path('remo/<int:id>/',delete_cart),
    path('cartbuy/<int:id>/',buyme),
    path('customerdet/',customerdet),
    path('succ/',ordersummary)


]



