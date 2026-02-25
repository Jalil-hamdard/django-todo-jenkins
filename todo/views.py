from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    status_filter = request.GET.get('filter') # Get the 'filter' from URL
    
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")

    # Start with all tasks
    tasks = Task.objects.all().order_by('-id')

    # Apply filtering logic
    if status_filter == 'completed':
        tasks = tasks.filter(completed=True)
    elif status_filter == 'pending':
        tasks = tasks.filter(completed=False)

    # Calculate stats for the dashboard
    context = {
        "tasks": tasks,
        "total_count": Task.objects.count(),
        "pending_count": Task.objects.filter(completed=False).count(),
        "completed_count": Task.objects.filter(completed=True).count(),
        "current_filter": status_filter,
    }
    return render(request, "todo/task_list.html", context)
    
def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    # This toggles the status: if True, becomes False; if False, becomes True
    task.completed = not task.completed 
    task.save()
    return redirect("task_list")

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("task_list")
