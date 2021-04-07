from django.urls import path
from . import views
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'home', views.HomeViewSet)

urlpatterns = [
    path('',views.home),
    path('<str:ver>', views.get_model_detail),
    path('<str:ver>/add', views.add_model_to_db),
    path('home/test_swagger', views.test_swagger.as_view()),
]

