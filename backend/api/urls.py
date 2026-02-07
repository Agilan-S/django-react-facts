from django.urls import path,include
from .views import get_facts, home

urlpatterns = [
    path('', home),
    path('facts/', get_facts),
    path('api/', include('api.urls')),

]

