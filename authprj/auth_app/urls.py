from django.urls import path
from . import views

app_name = "auth_app"

urlpatterns = [
    path('register/', views.register , name='registered'),
]