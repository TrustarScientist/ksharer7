from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'core/homepage.html')


@login_required
def feed(request):
    return render(request, 'core/feed.html')

@login_required
def resources(request):
    return render(request, 'core/resources.html')

@login_required
def messaging(request):
    return render(request, 'core/messaging.html')


@login_required
def notifications(request):
    return render(request, 'core/notifications.html')

@login_required
def profile(request):
    return render(request, 'core/profile.html')




