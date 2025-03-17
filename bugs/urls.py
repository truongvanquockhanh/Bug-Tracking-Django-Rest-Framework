from django.urls import path
from bugs import views



urlpatterns = [
    path('', views.BugsList.as_view()),
    path('filter/', views.FilterBugs.as_view()),
    path('detail/<int:pk>', views.BugsDetail.as_view()),
    path('sort/', views.SortBugs.as_view()),
]
