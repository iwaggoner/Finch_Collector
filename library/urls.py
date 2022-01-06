from django.urls import path
from .views.dogs_view import DogsView, DogDetailView
from .views.owner_view import OwnerView

urlpatterns = [
    path('dogs', DogsView.as_view(), name='dogs'),
    path('<int:pk>/', DogDetailView.as_view(), name='Dog-detail'),
    path('owners', OwnerView.as_view(), name='owners'),
]