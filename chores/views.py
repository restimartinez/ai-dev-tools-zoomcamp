from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """Simple landing page for signed-in family members."""
    return render(request, 'chores/home.html')
