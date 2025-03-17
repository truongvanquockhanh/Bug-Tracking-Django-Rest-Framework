from django.urls import path
from users import views



urlpatterns = [
    path('', views.UserList.as_view()),
    path('filter/', views.FilterUser.as_view()),
    path('detail/<int:pk>', views.UserDetail.as_view()),
    path('sort/', views.SortUser.as_view()),
]
