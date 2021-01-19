from django.urls import path

# from . import views
from .views import *

urlpatterns = [
    path('<int:id>/', get_by_id),
    # path('^', views.get_planet_by_pop)
    path('population/<int:population>/', get_planet_by_pop)
]