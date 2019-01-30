from desafioLucas.models import Link
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.shortcuts import redirect


# Create your views here.
class LinkCriado(CreateView):
    model = Link
    campos = ['url']

    def form_valid(self, form):
        prev = Link.objects.filter(url=form.instance.url)
        if prev:
            return redirect("mostar_link", pk=prev[0].pk)
        return super(LinkCriado, self).form_valid(form)


class MostrarLink(DetailView):
    model = Link


class MostrarUrlGrande(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs["short_url"]
        return Link.expand(short_url)