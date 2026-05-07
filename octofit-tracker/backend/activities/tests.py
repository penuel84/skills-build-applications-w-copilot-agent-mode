from django.test import TestCase
from django.contrib.auth.models import User
from .models import Activity, Workout

class ActivityModelTest(TestCase):
	def test_create_activity(self):
		user = User.objects.create(username='testuser')
		activity = Activity.objects.create(user=user, activity_type='run', duration=30, calories=300)
		self.assertEqual(str(activity), f"{user.username} - run - {activity.date}")

class WorkoutModelTest(TestCase):
	def test_create_workout(self):
		user = User.objects.create(username='testuser')
		workout = Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session', duration=45, calories_burned=400)
		self.assertEqual(str(workout), f"{user.username} - Morning Cardio - {workout.date}")
from django.test import TestCase

# Create your tests here.
