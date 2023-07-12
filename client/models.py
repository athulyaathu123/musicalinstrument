from django.db import models
from store.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")
    
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    options=(
        ("Order Placed","Order Placed"),
        ("Shipped","Shipped"),
        ("Out For Delivery","Out For Delivery"),
        ("Delivered","Delivered"),
        ("Cancel","Cancel")
    )
    status=models.CharField(max_length=100,choices=options,default="Order Placed")
    date=models.DateField(auto_now_add=True)