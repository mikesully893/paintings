from django.urls import path

from .views import PaintingListView, PaintingDetailView, SearchResultsListView, AcrylicListView, ResinListView


urlpatterns = [
    path('', PaintingListView.as_view(), name='painting_list'),
    path('<uuid:pk>', PaintingDetailView.as_view(), name='painting_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('acrylic/', AcrylicListView.as_view(), name='acrylic_list'),
    path('resin/', ResinListView.as_view(), name='resin_list'),
]