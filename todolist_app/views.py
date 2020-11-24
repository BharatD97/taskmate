from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist(request):
    if request.method == "GET":
        all_tasks = TaskList.objects.filter(manager = request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {"all_tasks" : all_tasks})
    else:
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request, 'New task added successfully!')
        return redirect('todolist')

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request, 'Access Denied! Requesting unauthorised access! Login via correct user account!')
    return redirect('todolist')

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, 'Access Denied! Requesting unauthorised access! Login via correct user account!')
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, 'Access Denied! Requesting unauthorised access! Login via correct user account!')
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "GET":
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', { 'task_obj' : task_obj })
    else:
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task edited successfully!')
        return redirect('todolist')

def about(request):
    context = {
        "about_text" : "Welcome to About Us!",
    }
    return render(request, 'about.html', context)

def index(request):
    context = {
        "index_text" : "Welcome to HomePage!",
    }
    return render(request, 'index.html', context)

def blog(request):
    context = {
        "blog_text" : "Welcome to Blog!",
    }
    return render(request, 'blog.html', context)

def contact(request):
    context = {
        "contact_text" : "Welcome to Contact Us!",
    }
    return render(request, 'contact.html', context)