"""
Script to populate the octofit_db database with test data
Run with: python manage.py shell < populate_db.py
"""

from django.contrib.auth.models import User
from api.models import Team, Activity, Leaderboard, Workout, UserProfile

# Create test users
users_data = [
    {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
    {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
    {'username': 'mike_johnson', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Johnson'},
    {'username': 'sarah_williams', 'email': 'sarah@example.com', 'first_name': 'Sarah', 'last_name': 'Williams'},
]

users = []
for user_data in users_data:
    user, created = User.objects.get_or_create(
        username=user_data['username'],
        defaults={
            'email': user_data['email'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
        }
    )
    users.append(user)
    print(f"{'Created' if created else 'Found'} user: {user.username}")

# Create test teams
teams_data = [
    {'name': 'Fitness Warriors', 'description': 'A team dedicated to fitness excellence'},
    {'name': 'Marathon Runners', 'description': 'For marathon enthusiasts'},
    {'name': 'Yoga Masters', 'description': 'Mindfulness and yoga practices'},
]

teams = []
for team_data in teams_data:
    team, created = Team.objects.get_or_create(
        name=team_data['name'],
        defaults={'description': team_data['description']}
    )
    teams.append(team)
    print(f"{'Created' if created else 'Found'} team: {team.name}")

# Create user profiles
for i, user in enumerate(users):
    if not hasattr(user, 'profile'):
        profile = UserProfile.objects.create(
            user=user,
            team=teams[i % len(teams)],
            bio=f"I am {user.first_name} {user.last_name}, passionate about fitness",
            age=20 + (i * 5),
            fitness_level=['beginner', 'intermediate', 'advanced'][i % 3]
        )
        print(f"Created profile for {user.username}")

# Create test activities
activities_data = [
    {'user_index': 0, 'type': 'running', 'title': 'Morning Run', 'duration': 30, 'distance': 5, 'calories': 300},
    {'user_index': 0, 'type': 'cycling', 'title': 'Evening Bike Ride', 'duration': 45, 'distance': 15, 'calories': 350},
    {'user_index': 1, 'type': 'yoga', 'title': 'Sunrise Yoga', 'duration': 60, 'distance': None, 'calories': 150},
    {'user_index': 1, 'type': 'swimming', 'title': 'Pool Swim', 'duration': 40, 'distance': 2, 'calories': 400},
    {'user_index': 2, 'type': 'gym', 'title': 'Weight Training', 'duration': 50, 'distance': None, 'calories': 450},
    {'user_index': 2, 'type': 'running', 'title': 'Afternoon Jog', 'duration': 25, 'distance': 4, 'calories': 250},
    {'user_index': 3, 'type': 'walking', 'title': 'City Walk', 'duration': 30, 'distance': 3, 'calories': 150},
    {'user_index': 3, 'type': 'cycling', 'title': 'Trail Ride', 'duration': 60, 'distance': 20, 'calories': 500},
]

for activity_data in activities_data:
    Activity.objects.get_or_create(
        user=users[activity_data['user_index']],
        activity_type=activity_data['type'],
        defaults={
            'title': activity_data['title'],
            'duration_minutes': activity_data['duration'],
            'distance_km': activity_data['distance'],
            'calories_burned': activity_data['calories'],
        }
    )
    print(f"Created activity: {activity_data['title']}")

# Create test workouts
workouts_data = [
    {
        'title': 'Beginner HIIT',
        'description': 'High Intensity Interval Training for beginners',
        'difficulty': 'beginner',
        'duration': 20,
        'calories': 250,
        'instructions': 'Alternate between 30 seconds of intense work and 30 seconds of rest'
    },
    {
        'title': 'Intermediate Running',
        'description': 'Distance running workout',
        'difficulty': 'intermediate',
        'duration': 45,
        'calories': 400,
        'instructions': 'Run at a steady pace for 45 minutes'
    },
    {
        'title': 'Advanced CrossFit',
        'description': 'Advanced CrossFit training',
        'difficulty': 'advanced',
        'duration': 60,
        'calories': 600,
        'instructions': 'Complete 5 rounds of the following: 10 burpees, 20 kettlebell swings, 30 box jumps'
    },
]

for workout_data in workouts_data:
    Workout.objects.get_or_create(
        title=workout_data['title'],
        defaults={
            'description': workout_data['description'],
            'difficulty_level': workout_data['difficulty'],
            'duration_minutes': workout_data['duration'],
            'target_calories': workout_data['calories'],
            'instructions': workout_data['instructions'],
        }
    )
    print(f"Created workout: {workout_data['title']}")

# Create leaderboards
for i, user in enumerate(users):
    leaderboard, created = Leaderboard.objects.get_or_create(
        user=user,
        defaults={
            'team': teams[i % len(teams)],
            'total_activities': (i + 1) * 2,
            'total_duration_minutes': (i + 1) * 100,
            'total_distance_km': (i + 1) * 15,
            'total_calories_burned': (i + 1) * 1000,
            'rank': i + 1,
        }
    )
    if created:
        print(f"Created leaderboard entry for {user.username}")

print("\nDatabase population complete!")
