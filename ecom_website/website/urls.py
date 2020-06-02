from django.conf.urls import url

from . import views

app_name = 'website'
'''
list of patterns for url for redirection
'''
urlpatterns = [
    url(r'^createAccount', views.CreateAccountFormView.as_view(), name='createAccount'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^addService', views.AddServiceFormView.as_view(), name='addService'),
    url(r'^PlaceOrder', views.PlaceOrder.as_view(), name='PlaceOrder'),
    url(r'^', views.LoginFormView.as_view(), name='login')
]
