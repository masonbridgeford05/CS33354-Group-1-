from PIL import Image
import random
from apps.game.models import GameImage

def genRandomImage(mode):
    image = GameImage.objects.filter(difficulty=mode)
    count = image.count()

    if count > 0:
        random_index = random.randint(0, count - 1)
        random_image = image[random_index]
    else:
        return None, None

    return random_image.image_path, random_image.location