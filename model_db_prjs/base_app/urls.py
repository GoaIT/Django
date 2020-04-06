from django.urls import path
from base_app import views

#app_name = "base_app"

urlpatterns = [
    path('',views.PostListViews.as_view(),name='post_list'),
    #tot ce urmeaza dupa /about sa apeleze fct AboutView din views.py
    path('about/$', views.AboutView.as_view(), name='about'),   
]