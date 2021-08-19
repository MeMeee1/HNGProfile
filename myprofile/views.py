from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView # new
from .models import New
from .forms import PostForm
from django.views.generic import TemplateView

class Postview(CreateView):
	model = New
	form_class = PostForm
	template_name = 'home.html'
	success_url = reverse_lazy('response')
	
class Thankview(TemplateView):
	template_name = 'response.html'
		
# Create your views here.
