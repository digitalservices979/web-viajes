from django import template

register = template.Library()

def precio(asientos, precio):
	return (precio*asientos)

def total(precio):
	mostrar=0
	for totales in precio:
		mostrar += (totales.pasajero.asientos*totales.lugar.precio)
	return mostrar

register.filter('precio',precio)

register.filter('total',total)