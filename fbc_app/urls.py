# fbc_app urls
from django.urls import path
from . import views

# set app name
app_name = 'fbc_app'

# url patterns
urlpatterns = [
    path('', views.UnveristyListView.as_view(), name='fbc_home'),
    path('university/<slug:pk>/', views.UniversityDetailView.as_view(), name="fbc_detail"),
    path('create/', views.UniversityCreateView.as_view(), name='fbc_create'),
    path('update/<slug:pk>/', views.UniversityUpdateView.as_view(), name='fbc_update'),
    path('delete/<slug:pk>/', views.UniversityDeleteView.as_view(), name='fbc_delete'),
]