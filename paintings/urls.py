from django.urls import path

from .views import PaintingListView, PaintingDetailView

urlpatterns = [
    path('', PaintingListView.as_view(), name='painting_list'),
    path('<uuid:pk>', PaintingDetailView.as_view(), name='painting_detail'),
]