from desafioLucas.models import Link
from django.views.generic.edit import CreateView

# Create your views here.
class LinkCriado(CreateView):
    model = Link
    campos = ['url']