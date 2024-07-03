from django.shortcuts import render
from .models import Tod

def todo_list(request):
    todos=Tod.objects.all()
    return (request,'todo/index.html',{'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        Tod.objects.create(title=title,description=description)
    return redirect('todo_list')


# Create your views here.
