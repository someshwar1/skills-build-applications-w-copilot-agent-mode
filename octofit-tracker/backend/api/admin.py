from django.contrib import admin
from .models import Team, Activity, Leaderboard, Workout, UserProfile


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'activity_type', 'duration_minutes', 'created_at']
    list_filter = ['activity_type', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'rank', 'total_calories_burned', 'total_distance_km']
    list_filter = ['rank', 'team']
    search_fields = ['user__username']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty_level', 'duration_minutes', 'target_calories']
    list_filter = ['difficulty_level', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'fitness_level', 'age', 'team']
    list_filter = ['fitness_level', 'team']
    search_fields = ['user__username']
    readonly_fields = ['created_at', 'updated_at']
