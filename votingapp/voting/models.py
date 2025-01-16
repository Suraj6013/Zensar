from django.db import models
from django.contrib.auth.models import User

class VoteObject(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_object = models.ForeignKey(VoteObject, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)