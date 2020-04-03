from django.shortcuts import render
from .forms import DateUser, DateProfil

# Create your views here.

def index(request):
    return render(request,'auth_app/index.html/')

def register(request):
    
    registered = False  #presupunem ca in prima instanta nu este inregistrat

    if request.method == "POST":

        user_form = DateUser(data=request.POST) #preia informatiile din campurile formei
        profile_form = DateProfil(data=request.POST)    #preia informatiile din campurile formei

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save() #aduna informatiile introduse in campul password
            user.set_password(user.password) #hash-uieste informatiile din campul password
            user.save()

            profile = profile_form.save(commit=False)   #verificam daca exista fotografie in campul imagine
            profile.user = user

            if 'profile_pic' in request.FILES:  #daca exista informatii in campul imagine
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = DateUser()
        profile_form = DateProfil()

    return render(request,'auth_app/registration.html',context={
                        'user_form':user_form,
                        'profile_form':profile_form,
                        'registered': registered,
                                                    })
