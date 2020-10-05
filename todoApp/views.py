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


