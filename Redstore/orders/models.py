from django.db import models
from customers.models import Customers
from products.models import Products
# Models for orders
class CartOrders(models.Model):
    LIVE = 1
    DELETE = 0
    CART_STAGE=0
    ORDER_CONFORMED=1
    ORDER_PROCCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE= (
                    (ORDER_PROCCESSED,'ORDER_PROCCESSED'),
                    (ORDER_DELIVERED,'ORDER_DELIVERED'),
                    (ORDER_REJECTED,'ORDER_REJECTED')
                   )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    DELETE_CHOICE = ((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
class OrderItems(models.Model):
    products=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,related_name='added_cart')  
    quantity=models.IntegerField(default=1) 
    owner=models.ForeignKey(CartOrders,on_delete=models.CASCADE,related_name='ordered_item')
   