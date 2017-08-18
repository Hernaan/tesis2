from __future__ import absolute_import
from django.contrib import admin
from apps.denuncias.models import Denuncia, Servicio, TipoServicio


admin.site.register(Denuncia)
admin.site.register(Servicio)
admin.site.register(TipoServicio)

