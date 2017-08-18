from __future__ import absolute_import
from django.shortcuts import render, get_object_or_404
from apps.denuncias.models import Denuncia, Servicio, TipoServicio
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from apps.denuncias.forms import DenunciaForm
from apps.denuncias.paginacion import Paginate
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin


def contacto(request):
	return render(request, 'denuncias/contacto_form.html')

def pgprincipal(request):
	return render(request, 'denuncias/index.html')

class listar(ListView):
	model = Denuncia
	template_name = 'denuncias/listar_denuncias.html'
	paginate_by = 10
	ordering = ['-id'] #Si no ordenamos como se muestra los datos no va a funcionar la notificacion

	@method_decorator(permission_required('denuncia.add_denuncia',reverse_lazy('denuncias:pgprincipal')))
	def dispatch(self, *args, **kwargs):
			return super(listar, self).dispatch(*args, **kwargs)
    
    	
        


def detail(request, denuncia_id):
	denuncia = get_object_or_404(Denuncia, pk=denuncia_id)
	return render(request, 'denuncias/detail.html', {'denuncia': denuncia})


class DenunciaCreate(SuccessMessageMixin,CreateView):
	context_object_name = "servicios"
	model = Denuncia
	form_class = DenunciaForm
	template_name = 'denuncias/denuncia_crear.html'
	success_url = reverse_lazy('denuncias:denuncia_crear')#redirigimos a una url de urls.py
	success_message = 'Gracias!!!! Ya recibimos tu denuncia'

	def get_context_data(self, **kwargs):
		context = super(DenunciaCreate, self).get_context_data(**kwargs)
		context['servicios'] = Servicio.objects.all()
		return context


def check_pubs(request):
	start = request.GET.get('date')
	today = datetime.now()
	pubs = Denuncia.objects.filter(fecha__range=(start, today)).count() - 1
	return JsonResponse({'num_pubs': pubs})

def listaDetalles(request):
	nombre_servicio = request.GET['servicio']
	# print "ajax nombre_servicio ", nombre_servicio

	result_set = []
	tipos_servicios = []
	pregunta = str(nombre_servicio[1:-1])
	# print "Pregunta: " + pregunta

	servicio_seleccionado = Servicio.objects.get(servicio = pregunta)
	# print "Nombre del servicio seleccionado: ", servicio_seleccionado
	all_tipoServicio = servicio_seleccionado.tiposervicio_set.all()
	
	for tipo in all_tipoServicio:
		# print "Tipo Servicio: ", tipo.Tipo_Servicio
		result_set.append({'TipoServicio': tipo.Tipo_Servicio})
		# print "Result_set: ", result_set
	return HttpResponse(json.dumps(result_set), content_type='application/json')