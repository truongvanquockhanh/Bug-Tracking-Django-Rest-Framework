from bugs.models import Bugs
from bugs.serializers import BugsSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.db.models import Q


# Create your views here.

class BugsList(generics.ListCreateAPIView):
    queryset = Bugs.objects.all()
    serializer_class = BugsSerializer


class BugsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bugs.objects.all()
    serializer_class = BugsSerializer

class FilterBugs(APIView):
     serializer_class = BugsSerializer

     def get(self, request, *args, **kwargs):
         
         status = request.query_params.get('status')
         priority = request.query_params.get('priority')
         
         bugs = Bugs.objects.filter(Q(status=status) |Q(priority=priority))
         serializer = BugsSerializer(bugs, many=True)

         return Response(serializer.data)
     
class SortBugs(APIView):

    serializer_class = BugsSerializer

    def get(self, request, format=None):

        sort = request.query_params.get('sort_by')
        bugs = Bugs.objects.all().order_by(sort)
        serializer = BugsSerializer(bugs, many=True)
        return Response(serializer.data)
