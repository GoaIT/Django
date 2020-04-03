from django import forms
from django.contrib.auth.models import User
from .models import AdaugaCampuriUseri

# aici definesti campurile pe care vrei sa le contina forma 


class DateUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())    #acest camp vrem sa-l modificam de asta este trecut aici. 

    class Meta():
        model = User
        fields = ('username','email','password')

class DateProfil(forms.ModelForm):
#aici nu trecem ceva pentru ca nu vrem sa modificam nici un camp
    class Meta():
        model = AdaugaCampuriUseri  #aici importi campurile din forma DateProfil
        fields = ('profile_site','profile_pic')