from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, Activity, Leaderboard, Workout, UserProfile


class TeamTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team', description='Test Description')
    
    def test_create_team(self):
        self.assertEqual(self.team.name, 'Test Team')
    
    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')


class ActivityTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            title='Morning Run',
            duration_minutes=30,
            calories_burned=300
        )
    
    def test_create_activity(self):
        self.assertEqual(self.activity.title, 'Morning Run')
        self.assertEqual(self.activity.user.username, 'testuser')
    
    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'testuser - running')


class LeaderboardTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.leaderboard = Leaderboard.objects.create(
            user=self.user,
            total_activities=5,
            total_calories_burned=1500,
            rank=1
        )
    
    def test_create_leaderboard(self):
        self.assertEqual(self.leaderboard.total_activities, 5)
        self.assertEqual(self.leaderboard.rank, 1)


class WorkoutTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            title='HIIT Workout',
            description='High Intensity Interval Training',
            difficulty_level='intermediate',
            duration_minutes=30,
            target_calories=400,
            instructions='Follow the routine'
        )
    
    def test_create_workout(self):
        self.assertEqual(self.workout.title, 'HIIT Workout')
        self.assertEqual(self.workout.difficulty_level, 'intermediate')


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(
            user=self.user,
            fitness_level='beginner',
            age=25
        )
    
    def test_create_profile(self):
        self.assertEqual(self.profile.fitness_level, 'beginner')
        self.assertEqual(self.profile.age, 25)


class APIEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
    
    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_teams_list(self):
        Team.objects.create(name='Test Team')
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
