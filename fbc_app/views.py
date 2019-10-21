from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models



# university list view
class UnveristyListView(ListView):
    context_object_name = 'universities'
    model = models.University
    
# university detail view
class UniversityDetailView(DetailView):
    context_object_name = 'university_details'
    model = models.University
    template_name = 'fbc_app/university_detail.html'
