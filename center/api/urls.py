from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('', views.ModelDlList.as_view()),
    path('<int:pk>/', views.ModelDlDetail.as_view()),
]