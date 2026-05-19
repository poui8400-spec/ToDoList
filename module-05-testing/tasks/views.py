from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def task_list(request):
    filter_by = request.GET.get('filter', 'all')
    tasks = Task.objects.all()

    if filter_by == 'active':
        tasks = tasks.filter(completed=False)
    elif filter_by == 'completed':
        tasks = tasks.filter(completed=True)

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'filter': filter_by,
    })


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully.')
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


def task_toggle(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
    return redirect('tasks:task_list')


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
