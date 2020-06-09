from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserDetail(models.Model):
    account = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name="User")
    name = models.CharField(max_length=50, verbose_name="Full Name")
    phoneNumber = models.IntegerField(unique=True, verbose_name="Phone Number")
    email = models.EmailField(unique=True, verbose_name="Email")
    city = models.CharField(max_length=20, verbose_name="City")
    pincode = models.IntegerField(verbose_name="Pin Code")
    customer = models.BooleanField(choices=[(True, 'Customer'), (False, 'Service Provider')], verbose_name="Type")

    def __str__(self):
        return str(self.account) + '___' + self.name + '___' + str(
            self.phoneNumber) + '___' + self.email + '___' + self.city + '___' + str(self.customer)


categories = [
    (0, "Food Delivery"),
    (1, "Assignment Complete")
]


class Service(models.Model):
    category = models.IntegerField(choices=categories, verbose_name="Category")
    description = models.TextField(help_text="Write a little bit about the service", verbose_name="Description")

    def __str__(self):
        return categories[self.category][1] + '___' + self.description


class Provider(models.Model):
    available = models.BooleanField(choices=[(True, 'Available'), (False, 'Busy')], verbose_name="Available")
    provider = models.ForeignKey(UserDetail, on_delete=models.DO_NOTHING, verbose_name="Service Provider", default=None)

    def __str__(self):
        return str(self.available) + '___' + self.provider.name


class ServiceDetail(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, verbose_name="Service Provider")
    price = models.IntegerField(verbose_name="Price")
    service = models.ForeignKey(Service, verbose_name="Service", on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.provider.provider.name) + '___' + str(self.price) + '___' + str(self.service.description)


class Order(models.Model):
    detail = models.ForeignKey(ServiceDetail, on_delete=models.DO_NOTHING, verbose_name="Service Provided")
    time = models.DateTimeField(auto_now=True, verbose_name="Order Placed At")
    active = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True,
                                 verbose_name="Service Not Completed")
    customer = models.ForeignKey(UserDetail, on_delete=models.DO_NOTHING, verbose_name="Customer")

    def __str__(self):
        return str(self.detail) + '___' + str(self.time) + '___' + str(
            self.active) + '___' + self.customer.name + '__-' + self.detail.provider.provider.name
