from __future__ import absolute_import
from django.conf.urls import url, include
from django.contrib import admin
from apps.denuncias.views import listar, detail, DenunciaCreate, pgprincipal, contacto, check_pubs, listaDetalles
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', login_required(pgprincipal), name='pgprincipal'),
	url(r'^(?P<denuncia_id>[0-9]+)/$', login_required(detail), name='detail'),
	url(r'^crear/', login_required(DenunciaCreate.as_view()), name='denuncia_crear'),
	url(r'^listar/', login_required(listar.as_view()), name='listar'),
	url(r'^contacto', login_required(contacto), name='contacto'),
	url(r'^check_pubs/$', check_pubs, name='check_pubs'),
	url(r'^detalles/', listaDetalles, name='listaDetalles'),
]