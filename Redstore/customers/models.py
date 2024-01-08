from django.db import models
from django.contrib.auth.models import User

# Models for customers
class Customers(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=100)
    price = models.FloatField()
    address = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    image = models.ImageField(upload_to='media/')
    phone_no = models.CharField(max_length=10)
    delete_status = models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
