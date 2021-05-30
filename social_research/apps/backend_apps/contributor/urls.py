from django.urls import path
from apps.backend_apps.contributor import views
 
urlpatterns = [
    path('add-contributor/', views.Contributor.add_contributor, name='add_contributor'),
    path('all-contributor/', views.Contributor.all_contributor, name='all_contributor'),
    path('view-contributor/<id>/', views.Contributor.view_contributor, name='view_contributor'),
    path('edit-contributor/<id>/', views.Contributor.edit_contributor, name='edit_contributor'),
    path('delete-contributor/<id>/', views.Contributor.delete_contributor, name='delete_contributor'),
]