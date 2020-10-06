from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = formtask()

    if request.method == 'POST':
        form = formtask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') 
    
    context = {'tasks': tasks, 'form' : form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = formtask(instance=task)

    if request.method == 'POST':
        form = formtask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/') 

    context = {'form' : form} 
    return render(request, 'tasks/update.html', context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item' :item}
    return render(request, 'tasks/delete.html' ,context)