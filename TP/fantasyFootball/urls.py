from django.urls import path

from . import views

urlpatterns = [
  path('', views.TeamListView.as_view(), name = 'main'),
  path('teams/', views.TeamListView.as_view(), name = 'team-list'),
  path('teams/<int:team_id>/edit', views.TeamEditView.as_view(), name = 'team-edit'),
  path('teams/delete/player', views.delete_player_from_team, name = 'delete-player-from-team'),
  path('login', views.LoginView.as_view(), name = 'login'),
  path('logout', views.logout, name = 'logout')
]