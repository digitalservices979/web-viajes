from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import datetime
from django.urls import reverse_lazy
from django import forms
from .models import Pasajero, Pasaje
from package.models import Internacionale
from django.views.generic.edit import DeleteView


# Create your views here.

def pasajero(request, id_internacionale):
	lugar = get_object_or_404(Internacionale,pk = id_internacionale)

	if request.method == 'POST':
		pasajero = Pasajero()
		pasajero.nombre = request.POST['nombre']
		pasajero.apellido = request.POST['apellido']
		pasajero.ciudad = request.POST['ciudad']
		pasajero.telefono = request.POST['telefono']
		pasajero.direccion = request.POST['direccion']
		pasajero.documento = request.POST['documento']
		pasajero.asientos = request.POST['asientos']
		f = request.POST['fecha']

		fecha = datetime.datetime.strptime(f,"%d/%m/%y").strftime("%Y-%m-%d")
		pasajero.fecha = fecha
		pasajero.save()

		pasaje = Pasaje()

		pasaje.pasajero = pasajero
		pasaje.lugar = lugar

		pasaje.save()

	return redirect('car_list', permanent=True)

class CarListView(ListView):
	template_name ='ticket/car.html'
	model = Pasaje

class CarDeleteView(DeleteView):
	template_name = 'ticket/car.html'
	model = Pasaje 
	success_url = reverse_lazy('contact')