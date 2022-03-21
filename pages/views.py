from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """The home page for the painting store"""
    template_name = 'home.html'


class AboutPageView(TemplateView):
    """Page containing general information"""
    template_name = 'about.html'
