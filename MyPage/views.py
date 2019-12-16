"""
This module handles the requests from Connected/urls.py.
"""

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# Django views: 
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/ 
# Django has prepared many class-based views for common use cases

class HelloDjango(TemplateView):
    template_name = 'test.html'
