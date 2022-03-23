from django.views.generic import ListView, DetailView

from .models import Painting


class PaintingListView(ListView):
    model = Painting
    context_object_name = 'painting_list'
    template_name = 'paintings/painting_list.html'


class PaintingDetailView(DetailView):
    model = Painting
    context_object_name = 'painting'
    template_name = 'paintings/painting_detail.html'
