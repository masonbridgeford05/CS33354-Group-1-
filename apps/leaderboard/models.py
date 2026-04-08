from django.db import models


class AllTimeLeaderboardEntry(models.Model):
    ranking = models.IntegerField(default=-1)
    user_id = models.IntegerField()
    score = models.IntegerField()
    game_id = models.IntegerField()



    
