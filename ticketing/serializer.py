from .models import Project, Issue, Sprint
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("name", "description", "owner")


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ("id", "title", "type", "status", "project")


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ("name", "start", "end", "project")
