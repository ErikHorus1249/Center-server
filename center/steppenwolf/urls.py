from django.conf.urls import url
from .views import FileView
from django.urls import path, include
from . import views

urlpatterns = [
    path('upload', views.FileView.as_view()),
    path('test', views.TestView.as_view())
]