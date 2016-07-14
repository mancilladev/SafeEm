from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'emmang/home.html')

@login_required
def portal(request):
    return render(request, 'emmang/portal.html')
