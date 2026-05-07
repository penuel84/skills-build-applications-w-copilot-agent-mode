from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from teams.models import Team
from activities.models import Activity

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes', created_by=None)
        dc = Team.objects.create(name='DC', description='DC superheroes', created_by=None)

        # Create Users (Superheroes)
        users = [
            User.objects.create(username='ironman', email='ironman@marvel.com'),
            User.objects.create(username='captainamerica', email='cap@marvel.com'),
            User.objects.create(username='spiderman', email='spiderman@marvel.com'),
            User.objects.create(username='batman', email='batman@dc.com'),
            User.objects.create(username='superman', email='superman@dc.com'),
            User.objects.create(username='wonderwoman', email='wonderwoman@dc.com'),
        ]
        # Add users to teams
        marvel.members.add(users[0], users[1], users[2])
        dc.members.add(users[3], users[4], users[5])

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='run', duration=30, calories=300)
        Activity.objects.create(user=users[1], activity_type='cycle', duration=60, calories=600)
        Activity.objects.create(user=users[2], activity_type='swim', duration=45, calories=450)
        Activity.objects.create(user=users[3], activity_type='run', duration=25, calories=250)
        Activity.objects.create(user=users[4], activity_type='cycle', duration=70, calories=700)
        Activity.objects.create(user=users[5], activity_type='swim', duration=50, calories=500)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))