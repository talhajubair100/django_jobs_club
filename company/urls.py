from django.urls import path
from .views import company_create_view, company_update_view

urlpatterns = [
    path('add/', company_create_view, name='company_add'),
    path('edit/', company_update_view, name='company_change'),
    # path('ajax/load-district/', load_district, name='ajax_load_district'), # AJAX
]