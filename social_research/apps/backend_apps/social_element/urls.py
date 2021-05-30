from django.urls import path
from apps.backend_apps.social_element import views
 
urlpatterns = [
    path('add-social-element/', views.Social_element.add_social_element, name='add_social_element'),
    path('all-social-element/', views.Social_element.all_social_element, name='all_social_element'),
    path('edit-social-element/<id>/', views.Social_element.edit_social_element, name='edit_social_element'),
    path('delete-social-element/<id>/', views.Social_element.delete_social_element, name='delete_social_element'),
]