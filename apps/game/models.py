from django.db import models
from PIL import Image
from apps.accounts.models import User

class GameImage(models.Model):
    image_id = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    location = models.CharField( max_length=50)
    image_path = models.ImageField(upload_to='GameImages/')

    def save(self, *args, **kwargs): # ← Django calls this automatically
        super().save(*args, **kwargs)  
        try:
            img = Image.open(self.image_path.path)
            if img.size != (1280, 720):
                img = img.resize((1280, 720))
                img.save(self.image_path.path)
        except (FileNotFoundError, ValueError):
            pass

    def __str__(self):
        return f"{self.location} - {self.difficulty}"

class GameResult(models.Model):
    game_result_id = models.IntegerField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    score = models.IntegerField()
    difficult = models.BooleanField()

    def __str__(self):
        return f"Game {self.game_result_id} - User {self.user_id} - Score {self.score} - Difficulty {'Hard' if self.difficult else 'Easy'}"




