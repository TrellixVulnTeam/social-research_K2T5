from django.urls import path
from apps.backend_apps.correlation import views
 
urlpatterns = [
    path('correlation/', views.Correlation.correlation, name='correlation'),
]