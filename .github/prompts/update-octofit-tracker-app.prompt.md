---
mode: agent
model: gpt-4o
---

# Django App Updates

Update the OctoFit Tracker Django application to support users, teams, activities, leaderboard, and workouts collections.

## Requirements

All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.

### Tasks

1. **Update settings.py**
   - Configure MongoDB connection for djongo
   - Set up CORS settings
   - Ensure ALLOWED_HOSTS includes localhost and codespace domain
   - Add required apps to INSTALLED_APPS

2. **Update models.py**
   - Create User model with authentication support
   - Create Team model for team management
   - Create Activity model for logging workouts
   - Create Leaderboard model for competitive rankings
   - Create Workout model for personalized suggestions
   - Ensure all models use djongo for MongoDB compatibility

3. **Update serializers.py**
   - Create serializers for all models
   - Ensure ObjectId fields are converted to strings
   - Add proper field validation and relationships

4. **Update urls.py**
   - Configure router for REST API endpoints
   - Use codespace environment variable for base URL
   - Ensure `/api/` points to api_root
   - Add all model endpoints

5. **Update views.py**
   - Create ViewSets for all models
   - Implement proper authentication
   - Add filtering and search capabilities

6. **Update tests.py**
   - Create test cases for all models
   - Add API endpoint tests
   - Test authentication and permissions

7. **Update admin.py**
   - Register all models in Django admin
   - Configure admin display and filters

## Important Guidelines

- Follow the instructions in `.github/instructions/octofit_tracker_django_backend.instructions.md`
- Always use Django's ORM for database operations
- Never change directories - point to the directory when issuing commands
- Don't start the Django app unless instructed to do so
