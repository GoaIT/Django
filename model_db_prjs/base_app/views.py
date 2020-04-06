from django.shortcuts import render
#TemplateView este clasa ce tine de CBV
from django.views.generic import (TemplateView, ListView)
from base_app.models import Post, Comments
from django.utils import timezone


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'    #am conectat clasa la pagina about.html

class PostListViews(ListView):
    model = Post

    def get_queryset(self): 
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published-date'))
    #ACEST FEL DE INTEROGARE ESTE IN DOCUMENTATIE CU DENUMIREA "Fields Lookups"
    #facem un query in baza de date
    #adu din Post toate obiectele si filtreaza-le in fct de published_date
    #si care sa fie LessThanOrEqualTo data publicarii si ordoneaza-le dupa aceasta data
    #in ordine descrescatoare (acel - din fata)

def index(request):
    return render(request,'index.html/')