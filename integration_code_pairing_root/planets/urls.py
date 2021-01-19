from django.urls import path

from .views import *

urlpatterns = [
    path('<int:id>/', get_by_id),
    path('population/<int:population>/', get_planet_by_pop)
]