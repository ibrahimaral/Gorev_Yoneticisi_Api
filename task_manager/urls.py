from django.urls import path
from .views import ProjectListCreateAPIView, ProjectTaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    #path ile manuel yönlendirme

    #proje crud işlemleri
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list-create"),

    #project id'mizin uuid formatında olduğunu belirtiyoruz - projeye bağlı görevler(task)
    path("projects/<uuid:project_id>/tasks/", ProjectTaskListCreateAPIView.as_view(), name = "project-task-list-create"),

    #tekil görev işlemleri (patch,delete)
    path("tasks/<int:task_id>/",TaskDetailAPIView.as_view(), name= "task-detail"),

]