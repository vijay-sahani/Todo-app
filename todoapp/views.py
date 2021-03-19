from typing import Text
from django.shortcuts import redirect, render
from .models import Todo
# Create your views here.
def index(request):
    # catprods = Product.objects.values('category', 'id')
    reminders=Todo.objects.values()
    # tasks=[items['Text'] for items in reminders]
    return render(request,'index.html',{'tasks':reminders})


def saveReminder(request):
    if request.method=='POST':
        task=request.POST['task']
        if len(task)>5:
            todo=Todo(Text=task)
            todo.save()
    return redirect('index')


def deleteReminder(request,id):
    task_id=Todo.objects.filter(Edit_id=id)
    task_id.delete()
    return redirect('index')

def updateReminder(request):
    if request.method=='POST':
        id=request.POST['id']
        update_text=request.POST['task']
        edit_id=Todo.objects.filter(Edit_id=id)
        edit_id.update(update_text)
    return redirect('indexs')