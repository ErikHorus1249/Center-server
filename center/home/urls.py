from django.urls import path
from . import views
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('home/test_swagger', views.test_swagger.as_view()),
    path('home/get_model/<str:ver>', views.get_model_by_version.as_view()),
    path('home/add_model_manual/<str:ver>/<str:url>', views.add_model_manual.as_view()),
]

