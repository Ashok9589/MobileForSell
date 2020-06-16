from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='listings'),
    path('<int:listing_id>', views.slisting, name='listing'),
    path('search', views.search, name='search'),
]