"""sign_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from sign_pro import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('accounts/login/', views.index),
    path('login', views.login, name="login"),
    path(r'event_manage/', views.event_manage),
    path('sign', include('sign.urls')),
    path('logout/', views.logout),
    path('search_name/', views.search_name),
    path(r'guest_manage/', views.guest_manage),
    path(r'sign_index/<eid>/', views.sign_index),
    path(r'sign_index_action/<eid>/', views.sign_index_action),
]