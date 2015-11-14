from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from forms import RegistrationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages


@csrf_exempt
@login_required(login_url='/login/')
def index(request):
    nombre = request.user.get_short_name()

    if((request.user.groups.filter(name='Administrador').exists()) or (request.user.is_superuser)):
        marca =1
    else:
        marca =0
    return render_to_response('commerce/index.html',{'nombre':nombre,'marca':marca})

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

@csrf_exempt
@login_required(login_url='/login/')
@user_passes_test(lambda u: u.groups.filter(name='Operador').count() == 0, login_url='/commerce/')
def usuarios(request):
    nombre = request.user.get_short_name()

    if((request.user.groups.filter(name='Administrador').exists()) or (request.user.is_superuser)):
        marca =1
    else:
        marca =0

    if request.POST: # If the form has been submitted...
        form = RegistrationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/commerce/') # Redirect after POST
    else:
        form = RegistrationForm()

    lista = User.objects.all()

    return render(request, 'commerce/Mantenimiento/usuarios.html', {'lista':lista, 'nombre':nombre,'marca':marca, 'form': form})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/commerce/')