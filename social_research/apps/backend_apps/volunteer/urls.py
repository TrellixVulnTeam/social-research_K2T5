from django.urls import path
from apps.backend_apps.volunteer import views
 
urlpatterns = [
    path('add-volunteer/', views.Volunteer.add_volunteer, name='add_volunteer'),
    path('all-volunteer/', views.Volunteer.all_volunteer, name='all_volunteer'),
    path('view-volunteer/<id>/', views.Volunteer.view_volunteer, name='view_volunteer'),
    path('edit-volunteer/<id>/', views.Volunteer.edit_volunteer, name='edit_volunteer'),
    path('delete-volunteer/<id>/', views.Volunteer.delete_volunteer, name='delete_volunteer'),
]