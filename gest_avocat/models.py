from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    titre = models.CharField(max_length=500)
    contenu = models.TextField()
    date_pub = models.DateField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
