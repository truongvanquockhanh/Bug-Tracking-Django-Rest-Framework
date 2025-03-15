from django.urls import path
from project import views



urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('detail/<int:pk>', views.ProjectDetail.as_view()),
]
