from django.contrib import admin
from .models import VoteObject, UserVote

admin.site.register(VoteObject)
admin.site.register(UserVote)