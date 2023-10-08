"""URL configuration for djangoToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('about', views.about, name="about-page"),
    path('todolist', views.task_list, name="task-list"),
    # path('todolist', views.TodolistView.as_view(), name="task-list"),
    path('todolist/<slug:slug>', views.SinglePostView.as_view(), name="single-task")
    # path('todolist/<slug:slug>', views.single_post, name="single-task")
]
