from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
import json
from package.models import Internacionale

# Create your views here.

class IndexPageView(TemplateView):

    template_name = "core/index.html"

class ContactPageView(TemplateView):

    template_name = "core/contact.html"
    

def search(request):
	if request.is_ajax():
		paquete = Internacionale.objects.filter(lugar__startswith= request.GET.get('lugar',True)).values('lugar', 'id_internacional')
		return HttpResponse(json.dumps(list(paquete)),content_type='application/json')
	else:
		return HttpResponse('Solo Ajax')

