import django.contrib.auth.forms
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
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required()
def delete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.delete()

    return HttpResponseRedirect("/todolist")


@login_required()
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


class SinglePostView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todolist/single_task.html"
    context_object_name = "task"


@login_required()
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/todolist")
    else:
        form = TaskForm()
    return render(request, "todolist/add_task.html", {"form": form})


@login_required()
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


class RegisterUserView(SuccessMessageMixin, CreateView):
    template_name = "todolist/register.html"
    success_message = "Your profile was created successfully!"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("homepage")


class LoginUserView(SuccessMessageMixin, auth_views.LoginView):
    success_message = "You have successfully logged in!"
    template_name = "todolist/login.html"


class LogoutUserView(auth_views.LogoutView):
    template_name = "todolist/homepage.html.html"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Successfully logged out.')
        return response


class UserProfileView(SinglePostView, LoginRequiredMixin):
    template_name = "todolist/profile.html"
    context_object_name = "user"
    model = CustomUser
