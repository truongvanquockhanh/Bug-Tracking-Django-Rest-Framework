from bugs.models import Bugs
from bugs.serializers import BugsSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView



# Create your views here.

class BugsList(generics.ListCreateAPIView):
    queryset = Bugs.objects.all()
    serializer_class = BugsSerializer


class BugsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bugs.objects.all()
    serializer_class = BugsSerializer