from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from authentication.serializers import AuthSerializer
from django.http import Http404
import bcrypt

UserModel = get_user_model()


class SettingsBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        user = UserModel.objects
        try:
            user = UserModel.objects.get(username = username)
        except :
            raise Http404("user don't exist")
        user = UserModel.objects.get(username = username)
        pw = AuthSerializer(user).data['password']
        print("filter name: ", user, pw)
        pwd_valid = bcrypt.checkpw(password.encode(), pw.encode())
        
        if pwd_valid and user:
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None