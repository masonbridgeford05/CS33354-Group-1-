from apps.leaderboard.models import LeaderboardEntry
from apps.game.models import GameResult

class LeaderboardController:

    def get_top_scores(self, limit=10):
        return GameResult.objects.all()[:limit]

    def get_top_scores_by_mode(self, gamemode, limit=10):
        return GameResult.objects.filter(gamemode=gamemode)[:limit]

    def get_user_scores(self, user_id):
        return GameResult.objects.filter(user_id = user_id)