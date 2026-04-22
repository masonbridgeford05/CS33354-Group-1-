from apps.leaderboard.models import LeaderboardEntry
from apps.accounts.models import User

class LeaderboardController:
    
    def save_score(self, user_id, game_instance):
        # Fetch the real User object
        try:
            user_obj = User.objects.get(userId=user_id)
        except User.DoesNotExist:
            return None

        entry = LeaderboardEntry.objects.create(
            user=user_obj,
            score=game_instance.getScore(),
            gamemode=game_instance.gamemode
        )
        return entry

    def get_top_scores(self, limit=10):
        # We use select_related to grab the usernames in one database hit (efficient!)
        return LeaderboardEntry.objects.select_related('user').all()[:limit]

    def get_top_scores_by_mode(self, gamemode, limit=10):
        return LeaderboardEntry.objects.filter(gamemode=gamemode).select_related('user')[:limit]

    def get_user_scores(self, user_id):
        return LeaderboardEntry.objects.filter(user__userId=user_id)