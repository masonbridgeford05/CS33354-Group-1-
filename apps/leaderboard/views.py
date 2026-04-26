from apps.leaderboard.LeaderboardController import LeaderboardController
from django.shortcuts import render
from django.db.models import Sum
from apps.accounts.models import User

def show_leaderboard(request):
    # This gets the total points for every user and orders them by the highest sum
    leaderboard_data = User.objects.annotate(
        total_points=Sum('gameresult__score') 
    ).order_by('-total_points')[:10]
    
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard_data})