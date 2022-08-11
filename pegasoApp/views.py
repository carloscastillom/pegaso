from logging.config import valid_ident
from pickle import NONE
from django.shortcuts import render, redirect
from .models import taskDB
from .forms import TaskForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or NONE)

        if form.is_valid():
            form.save()
            all_items =taskDB.objects.all()
            messages.success(request,('new item added'))
            return render(request, 'index.html', {'all_items':all_items})

    else:
        all_items =taskDB.objects.all()
        return render(request, 'index.html', {'all_items':all_items})


def delete(request, list_id):
    item = taskDB.objects.get(pk=list_id)
    item.delete()
    return redirect('home') 
    #taskdb.delete(id)
    #all_items =taskDB.objects.all()
    #return render(request, 'index.html', {'all_items':all_items})

