from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

from rest_framework import routers
from .views import UploadViewSet

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('/', include(router.urls)),
    path('', views.ModelDlList.as_view()),
    path('<int:pk>/', views.ModelDlDetail.as_view()),
    
]
# https://medium.com/@Joelhanson25/drf-how-to-make-a-simple-file-upload-api-using-viewsets-1b1e65ed65ca