from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def team_logo_path(instance, filename):
  return 'team_logos/{0}/{1}'.format(instance.team_name.replace(' ', ''), filename)

def player_pic_path(instance, filename):
  return 'player_pics/{0}_{1}/{2}'.format(instance.player_name.replace(' ', ''), instance.player_surname.replace(' ', ''), filename)

def stadium_image_path(instance, filename):
  return 'stadium_images/{0}/{1}'.format(instance.stadium_name.replace(' ', ''), filename)

def user_avatar_path(instance, filename):
  return 'user_avatars/{0}/{1}'.format(instance.user.username, filename)

class Team(models.Model):
  team_name = models.CharField(max_length = 100, db_index = True, unique = True)
  foundation_date = models.DateTimeField('date Founded')
  create_date = models.DateTimeField('date created')
  team_logo = models.FileField(upload_to = team_logo_path, default = '')
  description = models.TextField(default = '', blank = True)

  def __str__(self):
    return self.team_name

class Player(models.Model):
  team = models.ForeignKey(Team, on_delete = models.CASCADE, blank = True, null = True, related_name = 'players')
  player_position = models.CharField(max_length = 15, default = '')
  player_name = models.CharField(max_length = 30)
  player_surname = models.CharField(max_length = 30)
  player_picture = models.FileField(upload_to = player_pic_path, default = '', blank = True)
  
  def __str__(self):
    return self.player_name + ' ' + self.player_surname

class Stadium(models.Model):
  stadium_name = models.CharField(max_length = 50)
  stadium_image = models.FileField(upload_to = stadium_image_path, default = '')
  team = models.ForeignKey(Team, on_delete = models.CASCADE, blank = True, null = True, related_name = 'stadiums')
  description = models.TextField(default = '', blank = True)

  def __str__(self):
    return self.stadium_name

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_profile')
  manage_teams = models.ManyToManyField(Team)
  user_avatar = models.FileField(upload_to = user_avatar_path, default = '', blank = True)

  def manage_team(self, team_id):
    for t in self.manage_teams:
      return t.id == team_id

  def __str__(self):
    return self.user.username

class Match(models.Model):
  team_a = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'team_a')
  team_b = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'team_b')
  team_a_goals = models.SmallIntegerField()
  team_b_goals = models.SmallIntegerField()
  match_date = models.DateTimeField('date of match')
  stadium = models.ForeignKey(Stadium, on_delete = models.CASCADE)

  def __str__(self):
    return self.team_a + ' vs ' + self.team_b