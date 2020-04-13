from django import forms
from django.contrib.auth.models import User
from .models import UserOurModel

#Aici trebuie sa definim fiecare model pe care dorim sa-l avem pe pagina web
#chiar daca acesta este implicit sau facut de noi
#Obiectul User importat in forma dorita
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

#Obiectul nostru importat in formă
class UserOurForm(forms.ModelForm):
    class Meta():
        model = UserOurModel
        fields = ('portofolio_site','profile_pic')