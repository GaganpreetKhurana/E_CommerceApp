from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import CreateAccountForm,LoginForm,AddServiceDetail,PlaceOrder

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
                    print("login")
                    return redirect('website:login')
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
                    print("Login")
                    return redirect('website:login')
        return redirect('website:login')


@login_required(login_url='')
def logout_view(request):
    '''
    logout view
    :param request: request object
    :return: redirects to login
    '''
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
            price = form.cleaned_data['price']
            service = form.cleaned_data['service']
            form.save()
        return render(request, self.template_name, {'form': form})


class PlaceOrder(View):
    form_class = PlaceOrder
    template_name = 'website/order.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            service = form.cleaned_data['service']
            Place_Order = form.cleaned_data['active']
            form.save()
        return render(request, self.template_name, {'form': form})
