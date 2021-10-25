from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponse
from .serializers import TeamSerializer

from rest_framework import serializers, views, response, status, exceptions

from .models import Team

# Create your views here.
def index(request):
    list = Team.objects.all()
    context = {"teams": list}
    return render(request, "index.html", context)


class TeamListView(views.APIView):
    def get(self, request):
        teams = Team.objects.all()
        serialzed_teams = TeamSerializer(teams, many=True)
        return response.Response(serialzed_teams.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        team_to_add = TeamSerializer(data=request.data)

        if team_to_add.is_valid():
            team_to_add.save()
            return response.Response(team_to_add.data, status=status.HTTP_201_CREATED)

        return response.Response(team_to_add.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailView(views.APIView):
    def get_team_by_id(self, id):
        try:
            return Team.objects.get(id=id)
        except Team.DoesNotExist:
            raise exceptions.NotFound(detail="Hockey team does not exist")

    def get(self, request, id):
        team = self.get_team_by_id(id)
        serialized_team = TeamSerializer(team)
        return response.Response(serialized_team.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        team = self.get_team_by_id(id)
        team.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        team = self.get_team_by_id(id)
        updated_team = TeamSerializer(team, data=request.data)
        if updated_team.is_valid():
            updated_team.save()
            return response.Response(updated_team.data, status=status.HTTP_202_ACCEPTED)
        return response.Response(
            updated_team.errors, status=status.HTTP_400_BAD_REQUEST
        )
