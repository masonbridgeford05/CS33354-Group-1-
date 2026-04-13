from django.db import models

class LeaderboardEntry(models.Model):
    user_id = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    gamemode = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']  # highest score first

    def __str__(self):

      #  return f"{self.username} - {self.score}"

       return f"{self.user_id} - {self.score}"



    
