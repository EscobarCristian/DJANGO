from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic

from aplic3.models import Persona


def index(request):
	Persona= Persona.objects.all()
	return HttpResponse("Hola Mundo.aplic3")

class IndexView(generic.ListView):
	template_name = 'aplic3/index.html'
	context_object_name = 'persona_list'

	def get_queryset(self):
		   return Persona.objects.order_by('-id')