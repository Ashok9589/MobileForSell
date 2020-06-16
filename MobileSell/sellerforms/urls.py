from django.urls import path

from . import views

urlpatterns = [
    path('sell', views.sell, name='sell'),
    path('<int:slisting_id>', views.slisting, name='slisting'),
    path('index', views.index, name='slisting'),
]