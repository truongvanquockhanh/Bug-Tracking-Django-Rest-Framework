from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.http import  Http404

class LogOutSerialize(serializers.Serializer):
    refresh = serializers.CharField()


    def validate(self, attrs):
        
        self.token = attrs['refresh']

        return attrs

    def save(self, **kwargs):
        
        try:
            RefreshToken(self.token).blacklist()
        
        except TokenError:
            raise Http404("bad token")


