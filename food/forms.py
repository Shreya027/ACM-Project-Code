

from django import forms
from django.contrib.auth.models import User
 
class ContactForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField()
    notes = forms.CharField()
    image = forms.FileField()


class ListForm(forms.Form):
    destination = forms.CharField(initial='')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')    
   

