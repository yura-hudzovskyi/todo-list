from django.shortcuts import redirect
from django.views import generic

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    paginate_by = 3

    def get_queryset(self):
        return Task.objects.all()


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = "/"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = "/"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = "/"


def change_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("todo:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = "/tags/"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = "/tags/"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = "/tags/"

