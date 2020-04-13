from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView)
from base_app.models import Post, Comment
from base_app.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy # ne ajuta sa spunem catre ce pagina sa mergi dupa ce stergi un articol
from django.contrib.auth.mixins import LoginRequiredMixin #folosita pentru integrarea cu partea de creare postari. doar cei autentificati sa poata crea. Este
#un alias pentru decorators.

##### parte din curs Sectiunea 23, Modulul 168 din BootCampDjango 
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'    #am conectat clasa la pagina about.html

class PostListViews(ListView):  #obiectul care returneaza o lista cu toate articolele
    model = Post
    #metoda predefinita specifica ListView, care ne returneaza toate rezultatele filtrate
    def get_queryset(self): # in romaneste = setarea interogarii
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date") 
    #ACEST FEL DE INTEROGARE ESTE IN DOCUMENTATIE CU DENUMIREA "Fields Lookups"
    #facem un query in baza de date
    #adu din Post toate obiectele si filtreaza-le in fct de published_date
    #si care sa fie LessThanOrEqualTo data publicarii si ordoneaza-le dupa aceasta data
    #in ordine descrescatoare (acel - din fata), adica cele mai noi in fata
    
    #cum va arata pagina de prezentare articol. va afisa articolul
class PostDetailView(DetailView):
    model = Post

    #cum va arata pagina de creere articole
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'   # atribut din obiectul LoginRequiredMixin. cum se numeste pagina de logare.
    redirect_field_name = 'base_app/post_detail.html'   # ce se intampla dupa logare, pe ce pagina sa mearga
    form_class = PostForm   #importa forma PostForm definita in forms.py
    model = Post

    #cum arata pagina cand vrei sa updatezi un articol
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'   # atribut din obiectul LoginRequiredMixin. cum se numeste pagina de logare.
    redirect_field_name = 'base_app/post_detail.html'   # ce se intampla dupa logare, pe ce pagina sa mearga
    form_class = PostForm   #importa forma PostForm definita in forms.py
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('base_app/post_list.html') #dupa ce se sterge um articol merge catre pagina post_list

    #afiseaza pagina cu articolele nepublicate spre deosebire de PostListView care afiseaza cu cele publicate
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'base_app/post_list.html'
    model = Post
    # afiseaza doar articolele a caror camp null este = True, si le ordoneaza dupa data crearii
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
#^^^ parte din curs Sectiunea 23, Modulul 168 din BootCampDjango ^^^

# def index(request):
#     return render(request,'index.html/')

######################################################################################################################
#### Vezi curs BootCampDjango Sectiunea 23 Modulul 169 #####

# daca este apasat butonul Publish atunci se va salva in baza de date data publicarii si ne va redirectiona catre pagina articolului
@login_required
def post_publish(request,pk):
    post = get_list_or_404(Post,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)

@login_required #apelezei functia doar daca este conectat utilizatorul
def add_comment_to_post(request,pk):
    post = get_list_or_404(Post,pk=pk)  #ea continutul si trimitel lui Post la id = pk
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect('post_detail', pk=post.pk)  #pk=post.pk pentru ca aici ne referim expres la articol sa-i adaugam un comentariu
    else:
        form = CommentForm()
    return render(request,'base_app/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_list_or_404(Comment,pk=pk)    #apekezi modelul Comment cu pk pentru acel articol
    comment.approve()   #apelezi functia approve()
    return redirect('post_detail.html',pk=comment.post.pk)  #pk este al articolului care a primit un comentariu


@login_required
def comment_remove(request,pk):
    comment = get_list_or_404(Comment,pk=pk)    #sterge comentariul pentru articolul cu pk aferent articolului
    post_pk = comment.post.pk # in Modules.py, obiectul Comment are un atribut post care e FK la obiectului POST care are un pk ca PK
    #am salvat acest pk intr-o variabila pentru ca acel commentariu se va sterge si nu vom mai stii ce pk a avut.
    comment.delete()
    return redirect('post_detail.html',pk=post_pk)  #imi trebuie pk aici ca sa-l folosesc in urls.py pentru a sterge comentariul in fct de acesta

#^^^^ Vezi curs BootCampDjango Sectiunea 23 Modulul 169 ^^^^^