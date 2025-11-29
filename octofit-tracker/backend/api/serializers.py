from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'activity_type', 'title', 'description', 
                 'duration_minutes', 'distance_km', 'calories_burned', 'created_at', 'updated_at']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'id' in representation and isinstance(representation['id'], str):
            representation['id'] = str(representation['id'])
        return representation


class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team', 'total_activities', 'total_duration_minutes', 
                 'total_distance_km', 'total_calories_burned', 'rank', 'created_at', 'updated_at']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'id' in representation and isinstance(representation['id'], str):
            representation['id'] = str(representation['id'])
        return representation


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'difficulty_level', 'duration_minutes', 
                 'target_calories', 'instructions', 'created_at', 'updated_at']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'id' in representation and isinstance(representation['id'], str):
            representation['id'] = str(representation['id'])
        return representation


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'team', 'bio', 'profile_picture', 'age', 'fitness_level', 
                 'created_at', 'updated_at']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'id' in representation and isinstance(representation['id'], str):
            representation['id'] = str(representation['id'])
        return representation
