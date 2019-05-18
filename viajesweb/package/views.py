from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from .models import *

# Create your views here.

class PackageListView(ListView):
	template_name = 'package/packages.html'
	model = Internacionale
	paginate_by = 3

class PackageDetailView(DetailView):
	template_name = 'package/buy.html'
	model = Internacionale







