from django.urls import path

from todo.views import (
    TaskListView,
    change_task_status,
    TaskDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("change_task_status/<int:pk>/", change_task_status, name="change-task-status"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
