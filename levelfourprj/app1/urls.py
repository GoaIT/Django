from django.urls import path
from . import views

app_name = 'app_base' #acesta este tag-ul care va fi folosit in relative url templates

urlpatterns = [
    path('pag1/',views.pag1,name='pag1')    #totodata se mai foloseste numele ca si parametru dupa :
    
]