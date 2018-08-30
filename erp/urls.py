"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib.auth.decorators import login_required

import auth

from reports import views

urlpatterns = [
    path('apps', include('apps.urls')),
    path('admin/', admin.site.urls),
    path('auth/login/', auth.views.login_user),
    path('auth/logout/', auth.views.logout_user, name='logout'),
    path('hr', include('hrs.urls')),
    path('contacts', include('contacts.urls')),
    path('companies', include('companies.urls')),
    path('fms', include('fms.urls')),
    path('reports', views.index)
]

