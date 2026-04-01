import random
from django.test import TestCase
from apps.game.models import GameImage
from apps.game.GameController import GameController

class GameControllerTest(TestCase):


    def test_pick_random_image(self):
        controller = GameController(gamemode=0)
        image_path, location = controller.pick_random_image()
        
        # Check that a result is returned
        self.assertIsNotNone(image_path)
        self.assertIsNotNone(location)
        print(f"Random Image: {image_path}, Location: {location}")