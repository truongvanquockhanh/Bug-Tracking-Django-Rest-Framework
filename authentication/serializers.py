from rest_framework import serializers
from authentication.models import AuthUser


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'date_join']

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_join']