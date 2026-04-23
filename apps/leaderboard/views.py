from apps.leaderboard.LeaderboardController import LeaderboardController
from django.shortcuts import render
from apps.game.models import GameResult
from django.db.models import Max

def show_leaderboard(request):
    # This query gets the highest score for each user
    # It ensures the same person doesn't take up all 10 spots
    top_scores = GameResult.objects.values('user_id__userName', 'gamemode') \
            .annotate(max_score=Max('score')) \
            .order_by('-max_score')[:10]
    context = {
        'leaderboard_data': top_scores
    }
    return render(request, 'leaderboard.html', context)