from django.urls import path
from apps.backend_apps.analytics import views
 
urlpatterns = [
    path('analytics/', views.Analytics.analytics_report, name='analytics'),
]