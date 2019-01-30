from django.conf.urls import patterns, include, url
from desafioLucas.views import LinkCriado
from desafioLucas.views import MostrarLink
from desafioLucas.views import MostrarUrlGrande

urlpatterns = patterns('',
    url(r'^$', LinkCriado.as_view(), name='home'),
    url(r'^link/(?P<pk>\d+)$', MostrarLink.as_view(), name='link_show'),
    url(r'^r/(?P<short_url>\w+)$', MostrarUrlGrande.as_view(),
              name='redirect_short_url'),
)
