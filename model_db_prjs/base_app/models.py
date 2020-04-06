from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=None)  #conectam un user autorizat cu un autor
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=None,null=True)  #nu stim cand va fi postat sau daca va fi postat

    #functie care sa ne returneze data publicarii
    #va fi apelata in momentul in care este apasat butonul de publicare

    def publish(self):  #functie care se apeleaza cand apasam butonul POSTEAZA
        self.published_date = timezone.now()    #salveaza data in campul published_date
        self.save()
    
    #functie aprobare comentarii
    def approve_comments(self):
        return self.Comment.filter(approved_comment=True)

    def get_absolute_url(self): #ne returneaza pagina pe care vom merge dupa ce este postat articolul
        
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):  #la apelarea functiei se returneaza valoarea din titlu. Transforma valoarea obiectului titlu intr-un string
        return self.title

    # model care defineste partea de comentarii

class Comments(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=None) #conecteaza un comment cu o postare
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())  #cum apasa butonul posteaza cum ii ia data din acel moment
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self): #ne returneaza pagina pe care vom merge dupa ce este postat comentariu
        
        return reverse('post_list')

    def __str__(self):
        return self.text
