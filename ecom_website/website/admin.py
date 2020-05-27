from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Service)
admin.site.register(Provider)
admin.site.register(ServiceDetail)
admin.site.register(Order)