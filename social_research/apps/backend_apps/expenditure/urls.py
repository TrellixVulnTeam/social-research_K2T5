from django.urls import path
from apps.backend_apps.expenditure import views
 
urlpatterns = [
    path('add-expenditure/', views.Expenditure.add_expenditure, name='add_expenditure'),
    path('all-expenditure/', views.Expenditure.all_expenditure, name='all_expenditure'),
    path('view-expenditure/<id>/', views.Expenditure.view_expenditure, name='view_expenditure'),
    path('edit-expenditure/<id>/', views.Expenditure.edit_expenditure, name='edit_expenditure'),
    path('delete-expenditure/<id>/', views.Expenditure.delete_expenditure, name='delete_expenditure'),
]