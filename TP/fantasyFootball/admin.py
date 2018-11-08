from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Team, Player, Stadium, Profile

# Register your models here.

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
  model = Profile
  can_delete = False

# Define a new User profile
class UserProfile(BaseUserAdmin):
  inlines = (ProfileInline,)

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Stadium)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserProfile)