from django.urls import path
from .views import get_facts, home

urlpatterns = [
    path('', home),
    path('facts/', get_facts),
]

