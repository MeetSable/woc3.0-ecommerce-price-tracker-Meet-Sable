from django.db import models
from background_task import background
import sys

class User(models.Model):
    username = models.CharField(max_length=30)
    emailaddress = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=2000)
    product = models.CharField(max_length=500)
    site_title = models.CharField(max_length=20, default= "")
    desired_price = models.FloatField(default=0)
    last_checked_price = models.FloatField(default=sys.float_info.max)
    is_available_at_desired_price = models.BooleanField(default=False) 

    def __str__(self):
        return self.product
    
        
    



