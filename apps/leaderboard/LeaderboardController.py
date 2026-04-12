from apps.leaderboard.models import LeaderboardEntry

class LeaderboardController:
    
    def save_score(self, username, game_instance):
        entry = LeaderboardEntry.objects.create(
            username=username,
            score=game_instance.getScore(),
            gamemode=game_instance.gamemode,
            game_id=game_instance.getGameID()
        )
        return entry

    def get_top_scores(self, limit=10):
        return LeaderboardEntry.objects.all()[:limit]

    def get_top_scores_by_mode(self, gamemode, limit=10):
        return LeaderboardEntry.objects.filter(gamemode=gamemode)[:limit]

    def get_user_scores(self, username):
        return LeaderboardEntry.objects.filter(username=username)