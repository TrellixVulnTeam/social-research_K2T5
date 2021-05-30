from django.urls import path
from apps.backend_apps.elemental_fact import views
 
urlpatterns = [
    path('add-elemental-fact/', views.Elemental_fact.add_elemental_fact, name='add_elemental_fact'),
    path('all-elemental-fact/', views.Elemental_fact.all_elemental_fact, name='all_elemental_fact'),
    path('view-elemental-fact/<id>/', views.Elemental_fact.view_elemental_fact, name='view_elemental_fact'),
    path('edit-elemental-fact/<id>/', views.Elemental_fact.edit_elemental_fact, name='edit_elemental_fact'),
    path('delete-elemental-fact/<id>/', views.Elemental_fact.delete_elemental_fact, name='delete_elemental_fact'),
    path('contributors-in-research/', views.Elemental_fact.contributors_in_research, name='contributors_in_research'),
]