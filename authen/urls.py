from django.urls import path
from authen import views
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='log_in'),
    path('logout/', views.LogOut.as_view(), name='log_out'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

