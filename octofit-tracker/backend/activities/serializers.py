from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Activity
        fields = '__all__'