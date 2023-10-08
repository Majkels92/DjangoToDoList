from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Task, User
from datetime import datetime, timezone
from django.utils.timezone import localdate
# Create your views here.


def counting_time(deadline):
    current_time = datetime.now(timezone.utc)
    end_time = deadline
    delta = end_time - current_time
    return delta.days


def about(request):
    return render(request, "todolist/about.html")


def index(request):
    return render(request, "todolist/homepage.html")


def delete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.delete()

    return HttpResponseRedirect("/todolist")


# class TodolistView(ListView):
#     model = Task
#     template_name = "todolist/todolist.html"
#     context_object_name = "tasks"
#
#     # def get_context_data(self, **kwargs):
#     #     context = super(TodolistView, self).get_context_data(**kwargs)
#     #     for task in Task.objects.all():
#     #         task_obj = Task.objects.get(id=task.id)
#     #         task.time_left = counting_time(task_obj.deadline)
#     #     return context

def task_list(request):
    tasks = Task.objects.all().order_by('deadline')
    countdown = dict()
    for task in tasks:
        count = counting_time(task.deadline)
        countdown[task.id] = count
    context = {"tasks": tasks,
               "time_left": countdown
               }
    return render(request, "todolist/todolist.html", context)


class SinglePostView(DetailView):
    model = Task
    template_name = "todolist/single_task.html"
    context_object_name = "task"
