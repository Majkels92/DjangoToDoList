from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Task, User
# Create your views here.


def about(request):
    return render(request, "todolist/about.html")


def index(request):
    return render(request, "todolist/homepage.html")


class TodolistView(ListView):
    model = Task
    template_name = "todolist/todolist.html"
    context_object_name = "tasks"


def single_post():
    pass
