from django.urls import path
from apps.backend_apps.ssl_ecommerz import views
 
urlpatterns = [
    path('ssl/', views.Ssl_ecommerz.surface, name='ssl'),
]