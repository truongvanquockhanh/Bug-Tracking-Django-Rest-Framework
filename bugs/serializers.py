from rest_framework import serializers
from bugs.models import Bugs

class BugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = "__all__"

