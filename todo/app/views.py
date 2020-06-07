from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def index(request):
    obj = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    
    context = {'obj':obj,
        'form':form
        }
    return render(request, 'app/index.htm', context)

def todo_delete(request, id):
    form = Todo.objects.get(pk=id).delete()
    return redirect('index')

def todo_update(request, id):
    if request.method == "POST":
        obj = Todo.objects.get(pk = id)
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect ('index')
    else:
        obj = Todo.objects.get(pk = id)
        form = TodoForm(instance=obj)
        context = {'form':form}
    return render(request, 'app/index.htm', context)

def todo_delete_complete(request):
    form = Todo.objects.filter(complete = True)
    form.delete()
    return redirect('index')

def todo_delete_all(request):
    form = Todo.objects.all().delete()
    context = {"error" :  "Todo is Empty "}
    return render(request, 'app/index.htm', context)

def back_to_home(request):
    return redirect('index')