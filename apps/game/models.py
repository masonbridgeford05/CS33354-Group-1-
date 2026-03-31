from django.db import models
from PIL import Image

class GameImage(models.Model):
    image_id = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    location = models.CharField( max_length=50)
    image_path = models.ImageField(upload_to='GameImages/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saves to database first
        img = Image.open(self.image.path)  # opens the uploaded image
        if img.size != (1280, 720):        # checks if wrong size
            img = img.resize((1280, 720))  # resizes it
            img.save(self.image.path)      # overwrites with resized version

    def __str__(self):
        return f"{self.location} - {self.difficulty}"




