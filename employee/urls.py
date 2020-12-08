from django.urls import path
from .views import employe_create_view

urlpatterns = [
    path('add/', employe_create_view, name='employe_add'),
   # path('<int:pk>/', views.person_update_view, name='person_change'),
    #path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]