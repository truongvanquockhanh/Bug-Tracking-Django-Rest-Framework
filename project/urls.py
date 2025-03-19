from django.urls import path
from project import views



urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('<int:pk>', views.ProjectDetail.as_view()),
    path('<int:pk>/bugs/', views.BugsOfProject.as_view()),
]
