"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from firstapp import views
from django.urls import re_path
from django.views.generic import TemplateView
urlpatterns = [
    path("about/", TemplateView.as_view(template_name="about.html")),
    path("index2/", views.index2),
    path('users/<int:id>/<name>/', views.users),
    path("testdb/", views.create),

    path("index/", views.index),
    path("index/add-new-employee/", )
]
