
from rest_framework import serializers
from .models import Workout, Activity

class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Workout
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Activity
        fields = '__all__'