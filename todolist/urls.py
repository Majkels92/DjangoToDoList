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
    path('todolist/task/<slug:slug>', views.SinglePostView.as_view(), name="single-task"),
    path('todolist/delete/<int:task_id>', views.delete_task, name="delete-task"),
    path('todolist/add-task', views.add_task, name="add-task"),
    path('todolist/update/<slug:slug>', views.edit_task, name="update-task"),
    path('register', views.register_user, name="register")
]
