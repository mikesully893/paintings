from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """The home page for the painting store"""
    template_name = 'home.html'

