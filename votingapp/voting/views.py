from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import VoteObject, UserVote

def index(request):
    objects = VoteObject.objects.all()
    return render(request, 'index.html', {'objects': objects})

@login_required
def vote(request, object_id):
    obj = VoteObject.objects.get(id=object_id)
    user = request.user

    # Check if the user has already voted
    if UserVote.objects.filter(user=user, vote_object=obj).exists():
        return redirect('index')

    obj.votes += 1
    obj.save()

    # Record the user's vote
    UserVote.objects.create(user=user, vote_object=obj)

    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})