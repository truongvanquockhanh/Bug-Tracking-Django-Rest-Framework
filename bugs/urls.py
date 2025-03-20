from django.urls import path
from bugs import views


urlpatterns = [
    path('', views.BugsList.as_view()),
    path('<int:pk>', views.BugsDetail.as_view()),
    path('<int:pk>/notes/', views.NoteOfBugs.as_view()),
]
