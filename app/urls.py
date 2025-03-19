from django.contrib import admin
from rest_framework.response import Response
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('', include('home.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('auths/', include('authen.urls')),
    path('users/', include('users.urls')),
    path('projects/', include('project.urls')),
    path('bugs/', include('bugs.urls')),
    path('notes/', include('note.urls')),
]
