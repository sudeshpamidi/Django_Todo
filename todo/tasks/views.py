from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import *
from .forms import TasksForm
# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    form = TasksForm(request.POST)
    if request.method =='POST':
        if form.is_valid:
            form.save()
        return redirect ('/')

    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'tasks/list.html',context) 

def updateTask(request, id):
    try:        
        task = Tasks.objects.get(id=id)
        form = TasksForm( instance= task )
        if request.method == 'POST':
            form = TasksForm(request.POST, instance = task)
            if form.is_valid():
                form.save()
                return redirect ('/')
    except Tasks.DoesNotExist:
        raise Http404

    context ={'form' : form}
    return render(request, 'tasks/update_task.html',context)

def deleteTask(request, id):
    task = Tasks.objects.get(id=id)
    if request.method =="POST":
        task.delete()
        return redirect("/")
    context = {'task' : task}
    return render(request, 'tasks/delete_task.html',context)

