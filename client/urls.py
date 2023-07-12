from django.urls import path
from .views import*


urlpatterns = [
    path('register',Regview.as_view(),name="reg"),
    path('home',home.as_view(),name="home"),
    path('pro',product.as_view(),name="product"),
    path('lgout',Logoutview.as_view(),name="lgout"),
    path('idet/<int:pid>',Instrumentdetailview.as_view(),name="idet"),
    path('acart/<int:pid>',addcart,name="acart"),
    path('vcart',Cartview.as_view(),name="vcart"),
    path('delcart/<int:id>',deletecartitem,name="delcart"),
    path('checkout/<int:cid>',Checkoutview.as_view(),name="checkout"),
    path('order',Myorder.as_view(),name="myorder"),
    path('cancelorder/<int:id>',cancel_order,name="cancelorder"),
    path('search',Search.as_view(),name="search"),
    
    
]
