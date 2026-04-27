from django.core.management.base import BaseCommand

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Usuń dane
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Dodaj użytkowników
        users = [
            User(name='Bruce Wayne', email='bruce@dc.com', team='dc'),
            User(name='Clark Kent', email='clark@dc.com', team='dc'),
            User(name='Diana Prince', email='diana@dc.com', team='dc'),
            User(name='Tony Stark', email='tony@marvel.com', team='marvel'),
            User(name='Steve Rogers', email='steve@marvel.com', team='marvel'),
            User(name='Natasha Romanoff', email='natasha@marvel.com', team='marvel'),
        ]
        User.objects.bulk_create(users)

        # Dodaj zespoły
        teams = [
            Team(name='marvel', members=['tony@marvel.com', 'steve@marvel.com', 'natasha@marvel.com']),
            Team(name='dc', members=['bruce@dc.com', 'clark@dc.com', 'diana@dc.com']),
        ]
        Team.objects.bulk_create(teams)

        # Dodaj aktywności
        activities = [
            Activity(user='bruce@dc.com', activity='run', distance=5),
            Activity(user='tony@marvel.com', activity='cycle', distance=20),
            Activity(user='diana@dc.com', activity='swim', distance=2),
        ]
        Activity.objects.bulk_create(activities)

        # Dodaj leaderboard
        leaderboard = [
            Leaderboard(team='marvel', points=120),
            Leaderboard(team='dc', points=110),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Dodaj treningi
        workouts = [
            Workout(user='steve@marvel.com', workout='pushups', reps=50),
            Workout(user='clark@dc.com', workout='pullups', reps=30),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
