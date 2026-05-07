from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Team
        fields = '__all__'