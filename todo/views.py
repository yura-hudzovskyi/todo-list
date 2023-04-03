from django.shortcuts import redirect
from django.views import generic

from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"

    def get_queryset(self):
        return Task.objects.all()


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = "/"


def change_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("todo:index")
