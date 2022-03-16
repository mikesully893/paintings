from django.urls import path
from .views import HomePageView

urlpatterns = [
    # Home page
    path('', HomePageView.as_view(), name='home'),
]