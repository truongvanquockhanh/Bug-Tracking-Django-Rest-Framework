from authentication.models import AuthUser
from authentication.serializers import AuthSerializer, GetUserSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import  Http404
import bcrypt



class UserList(APIView):
    # permission_classes = (permissions.AllowAny,) # can acces not authentication

    def get(self, request, format=None):
        """
         List all snippets, or create a new snippet.
        """
        user = AuthUser.objects.all()
        serializer = GetUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            pw=str.encode(serializer.validated_data['password'])
            hash = bcrypt.hashpw(pw, bcrypt.gensalt(14))
            serializer.validated_data['password']=hash.decode('utf-8')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return AuthUser.objects.get(pk=pk)
        except AuthUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = GetUserSerializer(user)
        
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = AuthSerializer(user, data=request.data)
        if serializer.is_valid():
            pw=str.encode(serializer.validated_data['password'])
            hash = bcrypt.hashpw(pw, bcrypt.gensalt(14))
            serializer.validated_data['password']=hash
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Authentication(APIView):
    def post(seft, request, pk, format=None):
        user =  seft.get_object(pk)
        serializer = AuthSerializer(user)
        password = serializer.data['password'].encode('utf-8')
        data = request.data['password']
        print('password: ', type(password))
        print('data: ', type(data))
        if bcrypt.checkpw(data.encode(), password):
            print("True", password)
        else:
            print("false")
        return Response(data)