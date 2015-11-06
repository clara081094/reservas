from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import messages
#import RPi.GPIO as GPIO

@csrf_exempt
@login_required(login_url='/login/')
def index(request):
    nombre = request.user.get_short_name()
    return render_to_response('commerce/index.html',{'nombre':nombre})

@csrf_exempt
def login_user(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/commerce/')

    logout(request)
    state = "Ingrese su usuario y password"
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(60)
                login(request, user)
                return HttpResponseRedirect('/commerce/')
            else:
                state = "Su cuenta no existe, contacte con el administrador"
        else:
            state = "Su username y/o password son incorrectos."

    return render_to_response('commerce/login.html',{'state':state, 'username': username})