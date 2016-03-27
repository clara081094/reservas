from django import forms
from django.contrib.auth.models import User,Group
from models import Reserva,Cliente,Tarifa,Mensaje,Tipo,Estado
from django.forms.extras.widgets import SelectDateWidget 


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    first_name = forms.CharField(label='Nombres')
    last_name = forms.CharField(label='Apellido')
    username = forms.CharField(label='Usuario')
    groups = forms.CharField(label='Rol')
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'groups',
            ]

    def __init__(self, *args, **kwargs):#Sort interests alphabetically
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.order_by('name')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        if commit:
            user.save()
        return user


class ReservaForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    res_fecha = forms.DateField(widget=SelectDateWidget(), label='Fecha de hoy')
    res_cuentadm = forms.CharField(label='Numero de la cuenta de dinero movil')
    res_detalles = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 6}), label='Detalles')
    tarifa_tar = forms.ModelChoiceField(queryset=Tarifa.objects.order_by('tar_nombre'), label='Elegir tarifa de pago:')
    
    class Meta:
        model = Reserva   
        fields = [
            'res_fecha',
            'res_cuentadm',
            'res_detalles',
            'tarifa_tar',
            ]

class ClienteForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    cli_dni = forms.CharField(label='DNI')
    cli_nombres = forms.CharField(label='Nonmbres')
    cli_appaterno = forms.CharField(label='Apellido paterno')
    cli_apmaterno = forms.CharField(label='Apellido materno')
    cli_direcion = forms.CharField(label='Direccion')
    cli_celular = forms.CharField(label='Celular')
    cli_email = forms.EmailField(required=True, label='Email del cliente')
    cli_nac = forms.DateField(widget=SelectDateWidget(), label="Fecha de nacimiento")
    
    class Meta:
        model = Cliente  
        fields = [
            'cli_dni',
            'cli_nombres',
            'cli_appaterno',
            'cli_apmaterno',
            'cli_direcion',
            'cli_celular',
            'cli_email',
            'cli_nac',
            ]

class MensajeForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    men_nombre = forms.CharField(label='Nombre del mensaje')
    men_fechae = forms.DateField(widget=SelectDateWidget(), label='Fecha de emision ')
    men_contenido = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 6}), label='Contenido del mensaje ')
    tipo_tipo = forms.ModelChoiceField(queryset=Tipo.objects.all())

    class Meta:
        model = Mensaje 
        fields = [
            'men_nombre',
            'men_contenido',
            'men_fechae',
            'tipo_tipo',
            ]

    def __init__(self, *args, **kwargs):#Sort interests alphabetically
        super(MensajeForm, self).__init__(*args, **kwargs)
        self.fields['tipo_tipo'].queryset = Tipo.objects.order_by('tipo_nombre')
