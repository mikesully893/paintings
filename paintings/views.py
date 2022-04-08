from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Painting


class PaintingListView(ListView):
    model = Painting
    context_object_name = 'painting_list'
    template_name = 'paintings/painting_list.html'


class AcrylicListView(ListView):
    model = Painting
    Painting.artwork_type = 'acrylic'
    context_object_name = 'acrylic_list'
    template_name = 'paintings/acrylic_list.html'


class ResinListView(ListView):
    model = Painting
    Painting.artwork_type = 'resin'
    context_object_name = 'resin_list'
    template_name = 'paintings/resin_list.html'


class PaintingDetailView(DetailView):
    model = Painting
    context_object_name = 'painting'
    template_name = 'paintings/painting_detail.html'


class SearchResultsListView(ListView):
    model = Painting
    context_object_name = 'painting_list'
    template_name = 'paintings/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Painting.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
