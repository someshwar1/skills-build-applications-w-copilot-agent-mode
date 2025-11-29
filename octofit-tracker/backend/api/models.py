from django.db import models
from django.contrib.auth.models import User
from djongo import models as djongo_models


class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('walking', 'Walking'),
        ('gym', 'Gym'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories_burned = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='leaderboard')
    total_activities = models.IntegerField(default=0)
    total_duration_minutes = models.IntegerField(default=0)
    total_distance_km = models.FloatField(default=0.0)
    total_calories_burned = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboards'
        ordering = ['-total_calories_burned', '-total_distance_km']
    
    def __str__(self):
        return f"{self.user.username} - Rank {self.rank}"


class Workout(models.Model):
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=50, choices=DIFFICULTY_LEVELS)
    duration_minutes = models.IntegerField()
    target_calories = models.IntegerField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    fitness_level = models.CharField(
        max_length=50,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        default='beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_profiles'
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
