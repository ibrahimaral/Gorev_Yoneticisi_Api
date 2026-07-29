from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import logging
from .models import Project, Task
from .serializer import ProjectSerializer, TaskSerializer
from rest_framework.pagination import PageNumberPagination

# Hataları kaydetmek için logger yazıyoruz
logger = logging.getLogger(__name__)

# uç noktalara sadece giriş yapmış (tokene sahip) kullanıcıların erişmesini sağlar 
class BaseAuthAPIView(APIView):
    permission_classes = [IsAuthenticated]

class ProjectListCreateAPIView(BaseAuthAPIView):
    def get(self, request):
        try:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Proje oluştururken bir hata oluştu: {str(e)}")
            return Response({"error":"Proje getirilirken bir hata oluştu"},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                # veri doğruysa kaydeder
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"proje oluşturulurken hata oluştu: {str(e)}")
            return Response({"error":"proje oluşturulurken bir hata oluştu"}, status=status.HTTP_400_BAD_REQUEST)


class ProjectTaskListCreateAPIView(BaseAuthAPIView):
    def get(self, request, project_id):
        try:
            # projenin varlığı kontrol edilir
            project = Project.objects.get(id=project_id)
            tasks = Project.objects.filter(project=project)

            #filtreleme
            status__param = request.query_params.get("status")
            if status__param:

                #eğer urlde stastus parametresi varsa o duruma göre filtrele
                tasks = tasks.filter(status=status__param)

            #sayfalama
            paginator = PageNumberPagination()
            paginator.page_size = 5 #her sayfada max 5 görev gösterilebilir
            paginated_tasks = paginator.paginate_queryset(tasks, request)

            serializer =TaskSerializer(paginated_tasks, many=True)

            return paginator.get_paginated_response(serializer.data)
        except Project.DoesNotExist:
            return Response({"error":"Belirtilen proje bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görevler getirilirken hata oluştu: {str(e)}")
            return Response({"error":"görevler getirilirken bir hata oluştu"}, status=status.HTTP_400_BAD_REQUEST)


    #bir projenin altına yeri görevler ekler
    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)

            # gelen veriyi kopyalayıp project id manuel eklenir
            data = request.data.copy()
            data["project"] = project.id

            serializer = TaskSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error":"Belirtilen proje bulunamadı"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görev oluşturukurken bir hata oluştu: {str(e)}")
            return Response({"error":"görev oluşturulurken bir hata oluştu"}, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPIView(BaseAuthAPIView):
    # görevin belirli alanlarını günceller
    def patch(Self,request, task_id):
        try:
            task = Task.objects.get(il=task_id)
            # partinal true parametresi sayesinde sadece gönderilen veriler güncellenir
            serializer = TaskSerializer(task, data=request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error":"Görev bulunamadı"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görev güncellenirken hata oluştu: {str(e)}")
            return Response({"error":"Görev güncellenirken bir hata oluştu"}, status=status.HTTP_400_BAD_REQUEST)

    # Görevi siler
    def delete(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({"message":"Görev silindi"}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error":"Görev bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görev silirken hata oluştu: {str(e)}")
            return Response({"error":"Görev silirken bir hata oluştu"}, status=status.HTTP_400_BAD_REQUEST)
