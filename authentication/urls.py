from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication import views
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]

urlpatterns = format_suffix_patterns(urlpatterns)