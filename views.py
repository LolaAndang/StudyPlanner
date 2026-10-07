from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):
    total_tasks = Task.objects.count()
    pending_tasks = Task.objects.filter(status='Pending').count()
    recent_tasks = Task.objects.order_by('due_date')[:5]

    context = {
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'recent_tasks': recent_tasks,
    }
    return render(request, 'home.html', context)

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'Tasks.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'task': task})

def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.status == 'Pending':
        task.status = 'Completed'
    else:
        task.status = 'Pending'
    task.save()
    return redirect('task_list')