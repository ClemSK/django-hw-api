from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    coach = models.CharField(max_length=50)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return f"The {self.team_name} coached by {self.coach} ({self.id})"
