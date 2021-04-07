from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('<str:ver>', views.get_model_detail),
    path('<str:ver>/add', views.add_model_to_db),
]

