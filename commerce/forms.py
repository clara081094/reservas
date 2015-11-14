from django import forms
from django.contrib.auth.models import User,Group


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