from project.models import Project
from bugs.serializers import BugsSerializer
from bugs.models import Bugs
from project.serializers import ProjectSerializer, PostProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q
from django.http import Http404


class ProjectList(APIView):

    serializer_class = ProjectSerializer

    def get(self, request, format=None):

        order = request.query_params.get('order_by', 'id')
        name = request.query_params.get('name', False)
        status = request.query_params.get('status', False)
        priority = request.query_params.get('priority', False)
        owner_by = request.query_params.get('owner_by', False)
        members = request.query_params.get('members', False)
        list_filter = {'name': name, 'status': status, 'priority': priority, 'owner_by': owner_by, 'members': members}
        list_filter = {k: v for k, v in list_filter.items() if v}
        print(list_filter)
        query = Q()
        for key, value in list_filter.items():
            query = query & Q(**{key: value})
        project = Project.objects.filter(query).order_by(order)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        get_user = request.user
        serializer = PostProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner_by'] = get_user
            serializer.save()
            return Response("Created new project", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class BugsOfProject(APIView):

    serializer_class = BugsSerializer

    def get(self, request, pk, format=None):
        project = Project.objects.get(pk=pk)
        bugs = Bugs.objects.filter(project=project)
        serializer = BugsSerializer(bugs, many=True)
        return Response(serializer.data)


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
            return Response("You aren't member in this project", status=status.HTTP_401_UNAUTHORIZED)
        project = self.get_object(pk)
        serializer = BugsSerializer(project, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        if not self.isMember(request, pk):
            return Response("You aren't member in this project", status=status.HTTP_401_UNAUTHORIZED)
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        if not self.isMember(request, pk):
            return Response("You aren't member in this project", status=status.HTTP_401_UNAUTHORIZED)
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilterProject(APIView):

    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):

        name = request.query_params.get('name')
        status = request.query_params.get('status')
        priority = request.query_params.get('priority')
        project = Project.objects.filter(Q(name=name) | Q(status=status) | Q(priority=priority))
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


class SortProject(APIView):

    serializer_class = ProjectSerializer

    def get(self, request, format=None):

        sort = request.query_params.get('sort_by')
        project = Project.objects.all().order_by(sort)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)
