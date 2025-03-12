from users.models import User
from users.serializers import PostSerializer
from authen.serializers import LogOutSerialize
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import bcrypt

class SignUp(APIView):

    permission_classes = (permissions.AllowAny,) # can acces not authentication
    serializer_class = PostSerializer

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            pw=str.encode(serializer.validated_data['password'])
            hash = bcrypt.hashpw(pw, bcrypt.gensalt(14))
            serializer.validated_data['password']=hash.decode('utf-8')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogOut(APIView):
    
    serializer_class = LogOutSerialize

    def post(self, request):
        serialize = self.serializer_class(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()

        return Response(status=status.HTTP_204_NO_CONTENT)