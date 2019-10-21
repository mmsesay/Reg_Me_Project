# fbc_app urls
from django.urls import path
from . import views

# set app name
app_name = 'fbc_app'

# url patterns
urlpatterns = [
    path('', views.UnveristyListView.as_view(), name='fbc_home'),
    path('university/<slug:pk>/', views.UniversityDetailView.as_view(), name="fbc_detail"),
    path('university/create/', views.UniversityCreateView.as_view(), name='fbc_create'),
    path('university/update/', views.UniversityUpdateView.as_view(), name='fbc_update'),
    path('university/delete/', views.UniversityDeleteView.as_view(), name='fbc_delete'),
]