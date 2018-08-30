import pdb

from django.http import *
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    logout(request)
    invalid = False
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/apps')
        else:
            invalid = True
    return render(request, 'login.html', {'invalid': invalid })

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/auth/login')

def login_admin(request):
    return render(request, 'login-admin.html')

def ll_required():
    return redirect('/auth/login')

