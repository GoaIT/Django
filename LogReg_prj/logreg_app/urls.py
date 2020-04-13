from django.urls import path
from . import views

app_name = "logreg_app"

#Login/registration/index sunt tag-uri pe care le vom folosi in fisierele html (vezi base.html)
#cand dam click pe tag sa ne duca pe pagina configurata

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.user_login, name='login'),    
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout' )
]