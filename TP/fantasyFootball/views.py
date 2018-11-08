from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Team, Player

class MainView(TemplateView):
  template_name = 'fantasyFootball/index.html'

class TeamListView(generic.ListView):
  model = Team

  print(Team.objects.all)

  template_name = 'fantasyFootball/teams/list.html'

class TeamEditView(TemplateView):
  template_name = 'fantasyFootball/teams/edit.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['team'] = Team.objects.get(pk = kwargs.get('team_id'))
    context['players'] = Player.objects.filter(team__id = None)

    return context
  
  def post(self, request, **kwargs):
    player_id = request.POST['player_id']
    team_id = request.POST['team_id']

    team = Team.objects.get(pk = team_id)
    player = Player.objects.get(pk = player_id)
    player.team = team
    player.save()

    return redirect('team-edit', team_id = team_id)

def delete_player_from_team(request):
  player_id = request.POST['player_id']
  team_id = request.POST['team_id']

  if player_id is not None:
    player = Player.objects.get(pk = player_id)
    player.team = None
    player.save()

  return redirect('team-edit', team_id = team_id)

class LoginView(TemplateView):
  template_name = 'fantasyFootball/authentication/login.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['error'] = False

      return context

  def get(self, request, **kwargs):
    if request.user.is_authenticated:
      return redirect('main')
    
    return super().get(self, request, **kwargs)

  def post(self, request, **kwargs):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    
    if user is not None:
      login(request, user)
      return redirect('main')
    else:
      return render(request, 'fantasyFootball/authentication/login.html', { 'error': True })

def logout(request):
    django_logout(request)

    return redirect('main')