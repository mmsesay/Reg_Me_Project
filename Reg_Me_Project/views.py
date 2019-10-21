from django.shortcuts import render
from django.views.generic import View,TemplateView

# index view 
class indexView(TemplateView):
    template_name = 'index.html'
    