from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


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
        title = request.POST.get('title', '').strip()
        due_date = request.POST.get('due_date') or None
        if title:
            Task.objects.create(title=title, due_date=due_date)
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_form.html', {})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            task.title = title
            task.due_date = request.POST.get('due_date') or None
            task.completed = 'completed' in request.POST
            task.save()
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_form.html', {'task': task})


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
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
