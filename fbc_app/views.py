from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)
from . import models

# university create view
class UniversityCreateView(CreateView):
    # specifing the fields to create
    fields =  ('name', 'chancellor', 'location')
    model = models.University

# university update view
class UniversityUpdateView(UpdateView):
    # specifing the fields to update
    fields = ('name', 'chancellor')
    model = models.University

# university delete view
class UniversityDeleteView(DeleteView):
    model = models.University
    success_url =  reverse_lazy("fbc_app:fbc_detail")

# university list view
class UnveristyListView(ListView):
    context_object_name = 'universities'
    model = models.University
    
# university detail view
class UniversityDetailView(DetailView):
    context_object_name = 'university_details'
    model = models.University
    template_name = 'fbc_app/university_detail.html'
