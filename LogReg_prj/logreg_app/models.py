from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#noua baza de date va contine campurile din User si campurile definite aici
# 1 - facem corelatie intre modelul nostru si obiectul User. 
# recomandat este sa precizez daca campul poate ramane gol.
# 2 - definim campurile noastre pe care le mai dorim in pagina.
# 3 - locatia unde merg pozele incarcate. trebuie sa exista folderul in arborele '/media/'
# 4 - username este atribut defaul din obiectul User

class UserOurModel(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE) # 1
    
    portofolio_site = models.URLField(blank=True) # 2
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True) # 3
    
    def __str__(self):
        return self.user.username # 4