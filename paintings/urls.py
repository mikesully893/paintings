from django.urls import path

from .views import PaintingListView, PaintingDetailView, SearchResultsListView

urlpatterns = [
    path('', PaintingListView.as_view(), name='painting_list'),
    path('<uuid:pk>', PaintingDetailView.as_view(), name='painting_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]