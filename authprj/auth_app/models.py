from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdaugaCampuriUseri(models.Model):
    user = models.OneToOneField(User,on_delete=None)   #am creat o instanta pentru a adauga la baza deja existenta noi campuri

    profile_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='poze_profil',blank=True)

    def __str__(self):
        return self.user.username