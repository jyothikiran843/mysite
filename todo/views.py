import re
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import is_valid_path
from todo.forms import input_task
from todo.models import task

# Create your views here.

def todolist(request):
    if request.method=='POST':
        form=input_task(request.POST)
        if form.is_valid:
            form.save()
        else:
            form=input_task()
    else:
        form=input_task()
    tasklu=task.objects.all()
    return render(request,'todo.html',{'form':input_task,'tasks':tasklu})

def delete(request,pk=None):
    if pk:
        tas=get_object_or_404(task,pk=pk)
        tas.delete()
    return redirect('/todo')