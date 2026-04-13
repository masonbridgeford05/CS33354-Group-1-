from apps.game.models import GameResult

class LeaderboardController:
<<<<<<< HEAD
    
    def save_score(self, username, game_instance):

        entry = LeaderboardEntry.objects.create(



         #   username=username,
          #  score=game_instance.getScore(),
          #  gamemode=game_instance.gamemode,
           # game_id=game_instance.getGameID()



user_id=username,
    score=game_instance.getScore(),
    gamemode=game_instance.gamemode



        )
        return entry
=======
>>>>>>> 2c7b3034b240c31fb1983a8bbcaf1451b14b6f3e

    def get_top_scores(self, limit=10):
        return GameResult.objects.all()[:limit]

    def get_top_scores_by_mode(self, gamemode, limit=10):
        return GameResult.objects.filter(gamemode=gamemode)[:limit]

<<<<<<< HEAD
    def get_user_scores(self, username):

       # return LeaderboardEntry.objects.filter(username=username)

       return LeaderboardEntry.objects.filter(user_id=username)
=======
    def get_user_scores(self, user_id):
        return GameResult.objects.filter(user_id = user_id)
>>>>>>> 2c7b3034b240c31fb1983a8bbcaf1451b14b6f3e
