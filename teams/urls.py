from django.urls import path
from .views import TeamDetailView, index, TeamListView

urlpatterns = [
    path("", index),
    path("api/", TeamListView.as_view()),
    path("api/<int:id>/", TeamDetailView.as_view()),
]
