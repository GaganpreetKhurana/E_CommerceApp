from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Service,UserDetail,Provider,ServiceDetail,Order
from .forms import CreateAccountForm,LoginForm,AddServiceDetail,PlaceOrder,CreateUser

class CreateAccountFormView(View):
    '''
    form view to creating new account
    '''
    form_class = CreateAccountForm
    template_name = 'website/createAccount.html'

    def get(self, request):
        logout(request)
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # authenticate
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    profile = request.user
                    provider=get_object_or_404(UserDetail, account=request.user)    
                    if not provider.customer:
                        provider=get_object_or_404(Provider,provider=provider)
                        provider.available=True
                        provider.save()
                        print("login")
                        return redirect('website:addUserDetails')
                    print("login")
                    return redirect('website:PlaceOrder')
        return render(request, self.template_name, {'form': form})


class LoginFormView(View):
    '''
    form view for Login
    '''
    form_class = LoginForm
    template_name = 'website/login.html'

    def get(self, request):
        logout(request)
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    profile = request.user
                    provider=get_object_or_404(UserDetail, account=request.user)    
                    if not provider.customer:
                        provider=get_object_or_404(Provider,provider=provider)
                        provider.available=True
                        provider.save()
                        print("login")
                        return redirect('website:addUserDetails')
                    print("login")
                    return redirect('website:PlaceOrder')
        return redirect('website:login')


@login_required(login_url='')
def logout_view(request):
    '''
    logout view
    :param request: request object
    :return: redirects to login
    '''
    profile = request.user
    provider=get_object_or_404(UserDetail, account=request.user)    
    if not provider.customer:
        provider=get_object_or_404(Provider,provider=provider)
        provider.available=False
        provider.save()
    logout(request)
    print("logout")
    return redirect('website:login')

class AddServiceFormView(View):
    '''
    View For adding a service
    '''
    form_class = AddServiceDetail
    template_name = 'website/createAccount.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            provider=get_object_or_404(UserDetail, account=request.user)
            provider=get_object_or_404(Provider,provider=provider)
            obj.provider=provider
            obj.save()
            form=self.form_class(None)
        return render(request, self.template_name, {'form': form})


class PlaceOrder(View):
    form_class = PlaceOrder
    template_name = 'website/order.html'

    def get(self, request):
        form = self.form_class(None)
        items = ServiceDetail.objects.all()
        args = {'items':items,'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            customer=get_object_or_404(UserDetail, account=request.user)
            obj.customer = customer
            obj.active = True
            form.save()
        return render(request, self.template_name, {'form': form})

@login_required(login_url='')
def addUserDetailsFormView(request):
    '''
    View For Adding details
    '''
    form_class = CreateUser
    template_name = 'website/login.html'

    if request.GET:
        form = form_class(None)
        args = {'form': form}
        return render(request, template_name, args)
    else:
        form = form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            customer = form.cleaned_data['customer']
            profile = request.user
            obj.account=request.user
            obj.email=profile.email
            form.save()
            if not customer:
                provider=Provider(available=True,provider=obj)
            form=form_class(None)
        return render(request, template_name, {'form': form})
