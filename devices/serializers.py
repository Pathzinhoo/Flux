from .models import CollectedData
from rest_framework import serializers

class CollectedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedData
        fields = ['id','stac','created_at','data']