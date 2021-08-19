from django.shortcuts import render

from .models import Project,Issue
from .serializer import ProjectSerializer,IssueSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Projectview(APIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all

    def get(self,request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)


class Issueview(APIView):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all

    def get(self, request):
        projects = Issue.objects.all()
        serializer = IssueSerializer(projects, many=True)
        return Response(serializer.data)

