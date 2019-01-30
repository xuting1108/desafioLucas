from django.test import TestCase
from desafioLucas.models import Link
from django.urls import reverse

# Create your tests here.
#vai fazer o teste se a url ira encurtar
class MiniUrl(TestCase):
    def mini_teste(self):
        url= "http:/www.teste.com/"
        link= Link(url=url) #um objeto link importado de models, que sera encurtado pelo metodo link.mini
        url_pequena=Link.mini(link)
        self.assertLess(len(url_pequena,len(url))) #assert faz testes de true or false

    def teste_resgatar_link(self):
        url= "http:/www.teste.com/"
        link= Link(url=url)
        url_pequena= Link.mini(link)
        link.save()
        exp_url= Link.expand(url_pequena)#url extendida
        self.assertEqual(url, exp_url)
   #vai fazer o teste da homepage, se ele existe
    def teste_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertIn("form",response.context)