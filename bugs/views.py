from bugs.models import Bugs
from bugs.serializers import BugsSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.db.models import Q
from note.serializers import NoteSerializer
from note.models import Note


# Create your views here.
class BugsList(APIView):

    serializer_class = BugsSerializer

    def get(self, request, format=None):

        order = request.query_params.get('order_by', 'id')
        title = request.query_params.get('title', False)
        status = request.query_params.get('status', False)
        priority = request.query_params.get('priority', False)
        project = request.query_params.get('project', False)
        list_filter = {'title': title, 'status': status, 'priority': priority, 'project': project}
        list_filter = {k: v for k, v in list_filter.items() if v}
        query = Q()
        for key, value in list_filter.items():
            query = query & Q(**{key: value})
        bugs = Bugs.objects.filter(query).order_by(order)
        serializer = BugsSerializer(bugs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = BugsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Created new project", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class BugsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bugs.objects.all()
    serializer_class = BugsSerializer


class SortBugs(APIView):

    serializer_class = BugsSerializer

    def get(self, request, format=None):

        sort = request.query_params.get('sort_by')
        bugs = Bugs.objects.all().order_by(sort)
        serializer = BugsSerializer(bugs, many=True)
        return Response(serializer.data)


class NoteOfBugs(APIView):

    serializer_class = NoteSerializer

    def get(self, request, pk, format=None):
        bugs = Bugs.objects.get(pk=pk)
        note = Note.objects.filter(bugs=bugs)
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)
