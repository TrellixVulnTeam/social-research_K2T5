from django.urls import path
from apps.backend_apps.blog import views
 
urlpatterns = [
    path('add-blog/', views.Blog.add_blog, name='add_blog'),
    path('all-blog/', views.Blog.all_blog, name='all_blog'),
    path('view-blog/<id>/', views.Blog.view_blog, name='view_blog'),
    path('edit-blog/<id>/', views.Blog.edit_blog, name='edit_blog'),
    path('delete-blog/<id>/', views.Blog.delete_blog, name='delete_blog'),
    path('social-research-blog/', views.Blog.front_blog, name='front_blog'),
    path('social-research-blog-detail/<id>/', views.Blog.front_blog_detail, name='front_blog_detail'),
    path('social-research-outcome/', views.Blog.front_research, name='front_research'),
]