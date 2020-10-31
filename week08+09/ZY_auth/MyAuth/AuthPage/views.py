from django.shortcuts import render
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return HttpResponse("Hello World ! this is test_page")

def auth_page(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            global cd
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
        if user:
            username = cd['username']
            login(request,user)
            return render(request,'user_center.html',{'username': username})
        else:
            return HttpResponse("login failed")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request,'authform.html',{'form': login_form})