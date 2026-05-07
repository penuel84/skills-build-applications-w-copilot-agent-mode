from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Leaderboard

class TeamModelTest(TestCase):
	def test_create_team(self):
		user = User.objects.create(username='testuser')
		team = Team.objects.create(name='Test Team', description='desc', created_by=user)
		team.members.add(user)
		self.assertEqual(str(team), 'Test Team')

class LeaderboardModelTest(TestCase):
	def test_create_leaderboard(self):
		user = User.objects.create(username='testuser')
		team = Team.objects.create(name='Test Team', description='desc', created_by=user)
		leaderboard = Leaderboard.objects.create(team=team, user=user, score=100)
		self.assertEqual(str(leaderboard), f"{team.name} - {user.username} - 100")
from django.test import TestCase

# Create your tests here.
