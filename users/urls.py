from django.urls import path
from users import views
from authen import views as lgo



urlpatterns = [
    path('', views.UserList.as_view()),
    path('detail/<int:pk>', views.UserDetail.as_view()),
]
