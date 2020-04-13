from django.shortcuts import render
from django.views.generic import (TemplateView)
from .forms import UserForm,UserOurForm
#
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class IndexView(TemplateView):
    template_name = 'logreg_app/index.html'

def register(request):
    
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_our_form = UserOurForm(data=request.POST)

        if user_form.is_valid and user_our_form.is_valid:
            #salvam toate informatiile din campurile completate
            user = user_form.save()
            
            #salvam parola cu hash-ul prin apelarea metodei predefine 'set_password'
            user.set_password(user.password)
            user.save()
            
            #pentru a nu avea suprascrieri commit=False
            #salvam toate valorile din forma user_our_form in 'profile'
            profile = user_our_form.save(commit=False)
            
            #fct pentru a face relationare 1 la 1 cu campurile din obiectul User
            #este acelasi lucru cu ce am facut in models.py <user = models.OneToOneField(User,on_delete=models.CASCADE)>
            #variabila profile preia si campurile din forma UserForm si le salveaza pe toate in DB la final
            profile.user = user 

            #verificam daca s-a incarcat o imagine 
            #acest profile_pic este folderul in care vom salva fotografiile
            #este definit in models.py ca si upload_to
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            #salvam toate valorile in DB
            profile.save()

            registered = True #toate valorile au ajuns in DB

        else:   #daca datele nu sunt valide
            print(user_form.errors,user_our_form.errors)
            
    else:   #daca nu s-a apasat butonul Register din fisierul registration.html
        #afiseaza campurile goale in pagina web
        user_form = UserForm()
        user_our_form = UserOurForm()
    
    #definim dictionarul cu variabile care se vor apela in fisierele html.
    #definim pagina pe care se fac toate aceste inregistrati(adica fct register se apeleaza pe pe pagina registration.html)
    return render(request,'logreg_app/registration.html',
                                    {'user_form':user_form,
                                     'user_our_form':user_our_form,
                                     'registered':registered})

#FUNCTIE OPTIONALA                            
@login_required #decorator special pt a verifica daca user-ul este logat.
def special(request):
    return HttpResponse('Te-ai delogat cu succes!')

@login_required     #doar daca user-ul este logat se poate face delogarea
def user_logout(request):
    logout(request) #medota predefinita in Django
    return HttpResponseRedirect(reverse('logreg_app:index'))   #daca s-a delogat apeleaza index din urls.py

def user_login(request):
    #stocam valorile introduse in cele doua campuri din html (username si password)
    if request.method == 'POST':
        username = request.POST.get('usernam')
        password = request.POST.get('passwor')
        
        #facem autentificarea user-ului cu metoda autenticate importata
        user = authenticate(username=username,password=password)

        if user: #daca user-ul a trecut de procesul de autentificare
            if user.is_active: #daca user-ul este activ in DB facem login-ul cu metoda predefinita 'login'
                login(request,user)
                #dupa logare redirectionam user-ul catre pagina 'index'
                return HttpResponseRedirect(reverse('logreg_app:index')) 
            else:
                HttpResponse("User-ul nu este activ!")
        else:
            print('Username: {} / Password: {} are incorect'.format(username,password))
            return HttpResponse('Autentificarea a esuat. User-ul nu exista in DB')
    else:
        #daca metoda nu este POST, ramai pe pagina login.html
        return render(request,'logreg_app/login.html', {})