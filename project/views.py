from project.models import Project
from users.serializers import GetUserSerializer
from users.models import User
from project.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView


class ProjectList(APIView):

    serializer_class = ProjectSerializer
    
    def get(self, request, format=None):
        
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        for project in serializer.data:
            list_data = []
            for user_id in project['members']:
              list_member = User.objects.filter(id=user_id)
              member_data = GetUserSerializer(list_member, many=True)
              if member_data.is_valid:
                list_data.append(member_data.data[0]['username'])

            project['members'] = list_data

        return Response(serializer.data)
  
    def post(self, request, format = None):
       
       serializer = ProjectSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response("Created new project", status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
       

    


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer