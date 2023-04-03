from django.urls import path

from todo.views import (
    TaskListView,
    change_task_status,
    TaskDeleteView,
    TaskCreateView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("change_task_status/<int:pk>/", change_task_status, name="change-task-status"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "todo"
