from django.urls import path
from note import views



urlpatterns = [
    path('', views.NoteList.as_view()),
    path('detail/<int:pk>', views.NoteDetail.as_view()),
]
