from users.models import User
from users.serializers import PostSerializer, GetUserSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import  Http404
import bcrypt


class CreaterUser(APIView):

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
    


class UserList(APIView):

    serializer_class = GetUserSerializer
    def get(self, request, format=None):
        """
         List all snippets, or create a new snippet.`
        """
        user = User.objects.all()
        serializer = GetUserSerializer(user, many=True)
        return Response(serializer.data)

    

class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    serializer_class = GetUserSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = GetUserSerializer(user)
        
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = PostSerializer(user, data=request.data)
        if serializer.is_valid():
            pw=str.encode(serializer.validated_data['password'])
            hash = bcrypt.hashpw(pw, bcrypt.gensalt(14))
            serializer.validated_data['password']=hash
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


