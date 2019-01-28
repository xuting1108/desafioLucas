from django.db import models

# Create your models here.
#contem o campo de url
class Link(models.Model):
    url=models.URLField()

    @staticmethod
    def encurtar(link):
        l, _= Link.objects.get_or_create(url=link.url)# criacao de um objeto tipo link
        return str(l.pk)# criacao de uma pk que sera retornado na forma de string

#o metodo estatico ira retornar uma unica letra
    @staticmethod
    def expandir(slug):
        link_id= int(slug)
        l=Link.objects.get(pk=link_id)
        return l.url