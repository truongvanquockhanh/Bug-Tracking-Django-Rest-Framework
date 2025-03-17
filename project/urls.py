from django.urls import path
from project import views



urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('filter/', views.FilterProject.as_view()),
    path('detail/<int:pk>', views.ProjectDetail.as_view()),
    path('sort/', views.SortProject.as_view()),
]
