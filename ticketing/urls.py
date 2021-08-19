from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from .views import Projectview, Issueview

urlpatterns = [
    url("projects",Projectview.as_view()),
    url("issues",Issueview.as_view())
]