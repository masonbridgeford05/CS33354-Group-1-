from apps.game.models import GameResult

class LeaderboardController:

    # fetching the top 10 scores from GameResult database
    def get_top_scores(self, limit=10):
        return GameResult.objects.all()[:limit]

    # fetching the top 10 scores by mode from GameResult databas
    def get_top_scores_by_mode(self, gamemode, limit=10):
        return GameResult.objects.filter(gamemode=gamemode)[:limit]

    # fetching the all scores by user from GameResult databas
    def get_user_scores(self, user_id):
        return GameResult.objects.filter(user_id = user_id)