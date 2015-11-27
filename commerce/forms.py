from django import forms
from django.contrib.auth.models import User,Group
from models import Reserva,Cliente,Tarifa,Mensaje,Tipo,Estado
from django.forms.extras.widgets import SelectDateWidget 


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'last_name',
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
    res_fecha = forms.DateField(widget=SelectDateWidget())
    res_detalles = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 6}))
    tarifa_tar = forms.ModelChoiceField(queryset=Tarifa.objects.order_by('tar_nombre'))
    
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
    cli_email = forms.EmailField(required=True)
    cli_nac = forms.DateField(widget=SelectDateWidget())
    
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
    men_fechae = forms.DateField(widget=SelectDateWidget(), label='Fecha de emision ')
    men_contenido = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 6}), label='Mensaje ')
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
