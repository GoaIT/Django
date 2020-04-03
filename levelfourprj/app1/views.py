from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def pag1(request):
    return render(request,'pag1.html')