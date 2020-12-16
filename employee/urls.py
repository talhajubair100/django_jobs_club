from django.urls import path
from .views import employe_create_view, load_district, employe_update_view

urlpatterns = [
    path('add/', employe_create_view, name='employe_add'),
    path('edit/', employe_update_view, name='employe_change'),
    path('ajax/load-district/', load_district, name='ajax_load_district'), # AJAX
]