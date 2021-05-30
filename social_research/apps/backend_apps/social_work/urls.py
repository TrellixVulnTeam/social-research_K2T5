from django.urls import path
from apps.backend_apps.social_work import views
 
urlpatterns = [
    path('add-social-work/', views.Social_work.add_social_work, name='add_social_work'),
    path('all-social-work/', views.Social_work.all_social_work, name='all_social_work'),
    path('view-social-work/<id>/', views.Social_work.view_social_work, name='view_social_work'),
    path('edit-social-work/<id>/', views.Social_work.edit_social_work, name='edit_social_work'),
    path('delete-social-work/<id>/', views.Social_work.delete_social_work, name='delete_social_work'),
]