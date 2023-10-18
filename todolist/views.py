from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from .models import Task, CustomUser
from datetime import datetime, timezone
from django.utils.timezone import localdate
from .forms import TaskForm, CustomUserCreationForm
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
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


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/todolist")
    else:
        form = TaskForm()
    return render(request, "todolist/add_task.html", {"form": form})


def edit_task(request, slug):
    task = get_object_or_404(Task, slug=slug)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.slug = slugify(form["title"].value())
            form.save()
            return HttpResponseRedirect("/todolist/task/" + task.slug)
        return render(request, "todolist/edit_task.html", {"form": form, "task": task})
    else:
        form = TaskForm(instance=task)
        return render(request, "todolist/edit_task.html", {"form": form,
                                                           "task": task})


# def register_user(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Account created for {form.cleaned_data.get("username")}')
#             return HttpResponseRedirect("/")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "todolist/register.html", {"form": form})

class RegisterUserView(SuccessMessageMixin, CreateView):
    template_name = "todolist/register.html"
    success_message = "Your profile was created successfully"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("homepage")

