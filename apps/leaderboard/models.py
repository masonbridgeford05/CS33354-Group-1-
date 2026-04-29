from django.db import models
from apps.accounts.models import User

class LeaderboardEntry(models.Model):
    # Linking to the actual User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    gamemode = models.CharField(max_length=20, default="easy")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return f"{self.user.userName} - {self.score}"