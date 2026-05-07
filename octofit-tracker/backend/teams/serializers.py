
from rest_framework import serializers
from .models import Leaderboard, Team

class LeaderboardSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Leaderboard
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Team
        fields = '__all__'