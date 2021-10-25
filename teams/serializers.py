# from django.db.models import fields
from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            "team_name",
            "coach",
            "logo",
            # "__all__",
        ]
