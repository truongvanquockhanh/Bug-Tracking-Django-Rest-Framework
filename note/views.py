from note.models import Note
from note.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView



# Create your views here.

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer