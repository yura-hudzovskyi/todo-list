from django.urls import path

from todo.views import TaskListView, change_task_status, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("change_task_status/<int:pk>/", change_task_status, name="change-task-status"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todo"
