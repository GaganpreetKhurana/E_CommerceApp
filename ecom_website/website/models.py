from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetail(models.Model):
    account=models.OneToOneField(User,on_delete=models.DO_NOTHING,verbose_name="User")
    name=models.CharField(max_length=50,verbose_name="Full Name")
    phoneNumber=models.IntegerField(unique=True,verbose_name="Phone Number")
    email=models.EmailField(unique=True,verbose_name="Email")
    city=models.CharField(max_length=20,verbose_name="City")
    pincode=models.IntegerField(verbose_name="Pin Code")
    customer=models.BooleanField(choices=[(True,'Customer'),(False,'Service Provider')],verbose_name="Type")

categories=[
    (0,"Food Delivery"),
    (1,"Assignment Complete")
]
class Service(models.Model):
    category=models.IntegerField(choices=categories,verbose_name="Category")
    description=models.TextField(help_text="Write a little bit about the service",verbose_name="Description")

class Provider(models.Model):
    available=models.BooleanField(choices=[(True,'Available'),(False,'Busy')],verbose_name="Available")
    provider=models.ForeignKey(UserDetail,on_delete=models.DO_NOTHING,verbose_name="Service Provider",default=None)

class ServiceDetail(models.Model):
    provider=models.ForeignKey(Provider,on_delete=models.DO_NOTHING,verbose_name="Service Provider")
    price=models.IntegerField(verbose_name="Price")
    service=models.OneToOneField(Service,verbose_name="Service",on_delete=models.DO_NOTHING)

class Order(models.Model):
    detail=models.OneToOneField(ServiceDetail,on_delete=models.DO_NOTHING,verbose_name="Service Provided")
    time=models.DateTimeField(auto_now=True,verbose_name="Order Placed At")
    active=models.BooleanField(choices=[(True,'Yes'),(False,'No')],default=False,verbose_name="Service Completed")
    customer=models.ForeignKey(UserDetail,on_delete=models.DO_NOTHING,verbose_name="Customer")
    provider=models.ForeignKey(Provider,on_delete=models.DO_NOTHING,verbose_name="Service Provider")