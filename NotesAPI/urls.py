"""
URL configuration for NotesAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from Notes import urls as note_urls
from Users import urls as user_urls
from Dashboard import urls as dashboard_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/', include(note_urls)),
    path('api/users/', include(user_urls)),
    path('api/dashboard/', include(dashboard_urls)),
]

