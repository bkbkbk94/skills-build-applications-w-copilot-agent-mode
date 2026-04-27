from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=20)

class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)
    members = models.JSONField(default=list)

class Activity(models.Model):
    user = models.EmailField()
    activity = models.CharField(max_length=50)
    distance = models.FloatField()

class Leaderboard(models.Model):
    team = models.CharField(max_length=20)
    points = models.IntegerField()

class Workout(models.Model):
    user = models.EmailField()
    workout = models.CharField(max_length=50)
    reps = models.IntegerField()
