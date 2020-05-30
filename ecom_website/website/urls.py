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
    url(r'^', views.LoginFormView.as_view(), name='login')
]