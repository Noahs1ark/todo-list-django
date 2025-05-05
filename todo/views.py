from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm 
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data.get('fname')
            user.last_name = form.cleaned_data.get('lname')
            user.save()
            login(request, user)  
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
#view all tasks
@login_required(login_url='login')
def view_all_tasks(request):
    tasks=Task.objects.filter(user=request.user,completed=False)
    completed_tasks=Task.objects.filter(user=request.user,completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        'firstname':request.user.first_name,
        'lastname':request.user.last_name,
        }
    return render(request,'home.html',context)

def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk,user=request.user)
    task.completed = not task.completed
    task.save()
    tasks = Task.objects.filter(user=request.user, completed=False)
    completed_tasks = Task.objects.filter(user=request.user, completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        'firstname':request.user.first_name,
        'lastname':request.user.last_name,
        }
    return render(request, 'home.html', context)

#view details of each task
@login_required
def view_details(request,pk):
    task=get_object_or_404(Task,pk=pk)
    context={'task':task}
    return render(request,'task_details.html',context)

#creating anew task
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    context={'form':form}
    return render(request, 'task_edit.html', context)

#updating/editing tasks
@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list') 
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

#deleting tasks
@login_required
@require_POST
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list') 