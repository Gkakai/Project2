# from django.urls import path

# from .import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('/about', views.about, name='about'),
#     path('/contact', views.contact, name='contact'),
#     path('/agents', views.agents, name='agents'),
#     path('/properties', views.properties, name='properties'),
#     path('/services', views.services, name='services')
   

# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       # Root path, index view
    path('about', views.about, name='about'),   # About page
    path('contact', views.contact, name='contact'),  # Contact page
    path('agents', views.agents, name='agents'),  # Agents page
    path('properties', views.properties, name='properties'),  # Properties page
    path('services', views.services, name='services')  # Services page
]
