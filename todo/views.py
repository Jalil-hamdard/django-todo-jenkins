from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title: # Basic validation to prevent empty tasks
            Task.objects.create(title=title)
        return redirect("task_list")

    tasks = Task.objects.all().order_by('-id') # Shows newest tasks at the top
    return render(request, "todo/task_list.html", {"tasks": tasks})

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
