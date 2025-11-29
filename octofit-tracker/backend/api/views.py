from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout, UserProfile
from .serializers import (UserSerializer, TeamSerializer, ActivitySerializer, 
                         LeaderboardSerializer, WorkoutSerializer, UserProfileSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Activity.objects.all()
        return Activity.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkoutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def api_root(request):
    return Response({
        'users': request.build_absolute_uri('/api/users/'),
        'teams': request.build_absolute_uri('/api/teams/'),
        'activities': request.build_absolute_uri('/api/activities/'),
        'leaderboards': request.build_absolute_uri('/api/leaderboards/'),
        'workouts': request.build_absolute_uri('/api/workouts/'),
        'profiles': request.build_absolute_uri('/api/profiles/'),
    })
