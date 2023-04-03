from django.urls import path

from todo.views import TaskListView, change_task_status

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("change_task_status/<int:pk>/", change_task_status, name="change_task_status"),
]

app_name = "todo"
