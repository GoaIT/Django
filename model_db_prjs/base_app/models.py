from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)  #conectam un user autorizat cu un autor
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=None,null=True)  #nu stim cand va fi postat sau daca va fi postat

    #functie care sa ne returneze data publicarii
    #va fi apelata in momentul in care este apasat butonul de publicare
    # fct care se apeleaza la buton
    def publish(self):  #functie care se apeleaza cand apasam butonul POSTEAZA
        self.published_date = timezone.now()    #salveaza data in campul published_date
        self.save()
    
    #functie aprobare comentarii care se leaga de momentul in care comentariul este aprobat
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    # fct predefinita care ne ajuta sa luam o decizie in ce sa facem dupa ce a fost apasat butonul post
    # astfel, ne duce pe pagina post_detail(pe care o vom defini in views.py) si ne aloca la url nr Primary Key al articolului
    def get_absolute_url(self): #ne returneaza pagina pe care vom merge dupa ce este postat articolul
    
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):  #la apelarea functiei se returneaza valoarea din titlu. Transforma valoarea obiectului titlu intr-un string
        return self.title

    # model care defineste partea de comentarii

class Comment(models.Model):
    post = models.ForeignKey('base_app.Post',related_name='comments',on_delete=models.CASCADE) #conecteaza un comment cu o postare
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)  #cum apasa butonul posteaza cum ii ia data din acel moment
    approved_comment = models.BooleanField(default=False)
    
    #functie care se apeleaza la buton
    def approve(self):
        self.approved_comment = True
        self.save()

    #ne returneaza pagina pe care vom merge dupa ce este postat comentariu
    # dupa ce comentariul a fost aprobat ne vom intoarce pe pagina cu postari, post_list (pe care o vom defini in views.py)
    def get_absolute_url(self): 
        return reverse('post_list.html')

    def __str__(self):
        return self.text

##### functie pe care o vom folosi foarte des pentru ai spune ce sa faca dupa ce se apeleaza clasa din models.py
    # def get_absolute_url(self): 
    #     return reverse('post_list')