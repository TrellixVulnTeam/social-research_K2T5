"""social_research URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# For Media URL
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Access App's Urls
    path('access/', include('apps.access_apps.access.urls'), name='access'),

    # Backend App's Urls
    path('social_element/', include('apps.backend_apps.social_element.urls'), name='social_element'),
    path('elemental_fact/', include('apps.backend_apps.elemental_fact.urls'), name='elemental_fact'),
    path('correlation/', include('apps.backend_apps.correlation.urls'), name='correlation'),
    path('analytics/', include('apps.backend_apps.analytics.urls'), name='analytics'),
    path('volunteer/', include('apps.backend_apps.volunteer.urls'), name='volunteer'),
    path('social-work/', include('apps.backend_apps.social_work.urls'), name='social_work'),
    path('contributor/', include('apps.backend_apps.contributor.urls'), name='contributor'),
    path('expenditure/', include('apps.backend_apps.expenditure.urls'), name='expenditure'),
    path('blog/', include('apps.backend_apps.blog.urls'), name='blog'),
    path('contact/', include('apps.backend_apps.contact.urls'), name='contact'),
    path('ssl_ecommerz/', include('apps.backend_apps.ssl_ecommerz.urls'), name='ssl_ecommerz'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)