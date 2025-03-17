from project.models import Project
from users.serializers import GetUserSerializer
from users.models import User
from project.serializers import ProjectSerializer, PostProjectSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
from django.http import Http404
import jwt



class ProjectList(APIView):

    serializer_class = ProjectSerializer
    
    def get(self, request, format=None):

        project = Project.objects.all().order_by()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)
  
    def post(self, request, format = None):
       
        token = request.auth.token
        key = settings.SECRET_KEY
        payload = jwt.decode(token, key, algorithms='HS256')
        get_user = User.objects.get(id=payload['user_id'])
       
        serializer = PostProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner_by'] = get_user
            serializer.save()
            return Response("Created new project", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
       

    


class ProjectDetail(APIView):


    serializer_class = ProjectSerializer

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
    
    def isMember(self, request, pk):

        user_login = request.user.id
        project = self.get_object(pk)
        serializer = ProjectSerializer(project).data
        if (user_login in serializer['members']) or (user_login == serializer['owner_by']):
            return True
        return False

    def get(self, request, pk, format=None):
        if not self.isMember(request, pk):
            return Response("You aren't member in this project", status=status.HTTP_302_FOUND)
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        if not self.isMember(request, pk):
            return Response("You aren't member in this project", status=status.HTTP_302_FOUND)
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if not self.isMember(request, pk):
            return Response("You aren't member in this project", status=status.HTTP_302_FOUND)
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FilterProject(APIView):
     
     serializer_class = ProjectSerializer

     def get(self, request, *args, **kwargs):
         
         name = request.query_params.get('name')
         status = request.query_params.get('status')
         priority = request.query_params.get('priority')

         project = Project.objects.filter(Q(name=name) | Q(status=status) |Q(priority=priority))
         serializer = ProjectSerializer(project, many=True)

         return Response(serializer.data)
     
    

class SortProject(APIView):

    serializer_class = ProjectSerializer

    def get(self, request, format=None):

        sort = request.query_params.get('sort_by')
        project = Project.objects.all().order_by(sort)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)