from django.db import models
from PIL import Image

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




