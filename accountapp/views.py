from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import User


def user_login(request):
    if request.method =='POST':
        nickname = request.POST['nickname']
        password = request.POST['password']
        user = authenticate(request, nickname=nickname, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("login success")
        else:
            return HttpResponse("login fail")
    else:
        return HttpResponse("request fail")

def user_logout(request):
    logout(request)
    return HttpResponse("logout success")

def user_signup(request):
    if request.method =='POST':
        email = request.POST['email']
        nickname = request.POST['nickname']
        password = request.POST['password']

        user = User.object.create_user(email=email, nickname=nickname, password=password)

        return HttpResponse("signup success")
    else:
        return HttpResponse("signup fail")

@login_required
def user_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return HttpResponse("Delete success")
    else:
        return HttpResponse("Delete fail")
