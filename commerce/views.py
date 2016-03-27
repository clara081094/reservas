from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from forms import RegistrationForm, ReservaForm, ClienteForm, MensajeForm
from models import Cliente,Reserva,Mensaje,Estado
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import connection, transaction


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
                request.session.set_expiry(180)
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
    return HttpResponseRedirect('/usuarios/')

@csrf_exempt
def deleteu(request):

    if request.POST:
        borrar = request.POST['campo']
        User.objects.get(id=borrar).delete()

    return HttpResponseRedirect('/usuarios/')

@csrf_exempt
@login_required(login_url='/login/')
def reservar(request,guardac):
    nombre = request.user.get_short_name()
    existe = "reserva"
    if((request.user.groups.filter(name='Administrador').exists()) or (request.user.is_superuser)):
        marca =1
    else:
        marca =0


    #if "paraReserva" in request.POST:# If the form has been submitted...
    #    form = ReservaForm(request.POST) # A form bound to the POST data
    #    print ("esta aca")
    #    men= MensajeForm(request.POST)
    #    print(men)
    #    if form.is_valid(): # All validation rules pass
    #        if men.is_valid():
    #            men.save()
    #            form.save()
    #            return HttpResponseRedirect('/commerce/') # Redirect after POST
    #        else:
    #            print("formato mensaje invalido")
    #    else:
    #        print("formato reserva invalido")
                
    #else:
    form = ReservaForm()
    men = MensajeForm()

   # if "paraMensaje" in request.POST:# If the form has been submitted...
    #    men= MensajeForm(request.POST) # A form bound to the POST data
    #    if men.is_valid(): # All validation rules pass
    #        men.save()
    #else:
    #    men = MensajeForm()
    
    return render_to_response('commerce/Reserva/generarReserva.html', {'guardac':guardac,'existe':existe,'form': form,'marca':marca, 'men':men})

@csrf_exempt
@login_required(login_url='/login/')
def reservars(request):
    existe = "reserva"
    guardac = request.POST['cliente']
    print(guardac)
    #print(Cliente.objects.get(cli_id=guardac))
    form = ReservaForm(request.POST) # A form bound to the POST data
    men= MensajeForm(request.POST)
    if form.is_valid(): # All validation rules pass
        print("reserva validad")
        if men.is_valid():
            men.save()
            form.save()
            met = Mensaje.objects.latest('men_id')
            ret = Reserva.objects.latest('res_id')
            ret.estado_est=Estado.objects.get(est_id=3)
            ret.cliente_cli=Cliente.objects.get(cli_id=guardac)
            ret.mensaje_men=met
            ret.save()
            return HttpResponseRedirect('/reservas/')
        else:
            print(men)
            print("formato mensaje invalido")
    else:
        print("formato reserva invalido")

    return render_to_response('commerce/Reserva/generarReserva.html', {'guardac':guardac,'existe':existe,'form': form, 'men':men})

@csrf_exempt
@login_required(login_url='/login/')
def buscarDNI(request):

    existe = "inicio"
    guardac = ""
    
    if "paraCliente" in request.POST:

        cliente = ClienteForm(request.POST)
        if cliente.is_valid(): # All validation rules pass
            try:
                cliente.save()
                guardac = cliente.cli_id
                return reservar(request, guardac)
            except:
                return HttpResponseRedirect('/buscarc/')
        else:
            print("no se guardo")
    else:
        cliente = ClienteForm()

    if "paraDNI" in request.POST:
        dni = request.POST['dni']
        try:
            existe = Cliente.objects.get(cli_dni=dni)
            guardac = existe.cli_id;
            return reservar(request, guardac)
        except Cliente.DoesNotExist:
            existe = None
    
    return render(request, 'commerce/Reserva/generarReserva.html', {'existe':existe,'cliente':cliente})

@csrf_exempt
@login_required(login_url='/login/')
def reservas(request):
    nombre = request.user.get_short_name()

    if((request.user.groups.filter(name='Administrador').exists()) or (request.user.is_superuser)):
        marca =1
    else:
        marca =0

    #if request.POST: # If the form has been submitted...
    #    form = RegistrationForm(request.POST) # A form bound to the POST data
    #    if form.is_valid(): # All validation rules pass
    #        form.save()
    #        return HttpResponseRedirect('/commerce/') # Redirect after POST
    #else:
    #    form = RegistrationForm()

    lista = Reserva.objects.all()

    return render(request, 'commerce/Reserva/verReservas.html', {'lista':lista, 'nombre':nombre,'marca':marca})
 
@csrf_exempt
@login_required(login_url='/login/')
def mensajes(request):
    nombre = request.user.get_short_name()

    if((request.user.groups.filter(name='Administrador').exists()) or (request.user.is_superuser)):
        marca =1
    else:
        marca =0

    #if request.POST: # If the form has been submitted...
    #    form = RegistrationForm(request.POST) # A form bound to the POST data
    #    if form.is_valid(): # All validation rules pass
    #        form.save()
    #        return HttpResponseRedirect('/commerce/') # Redirect after POST
    #else:
    #    form = RegistrationForm()

    lista = Mensaje.objects.all()

    return render(request, 'commerce/Mensaje/verMensajes.html', {'lista':lista, 'nombre':nombre,'marca':marca})


