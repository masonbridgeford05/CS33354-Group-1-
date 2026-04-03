from django.test import TestCase
from apps.game.Image import GameImage
from apps.game.GameController import GameController

class GameControllerTest(TestCase):

    def setUp(self):
        GameImage.objects.create(
            image_id=1,
            difficulty=0,
            location="New York",
            image_path="GameImages/test.jpg"
        )

    def test_pick_random_image(self):

        # Test if there is an image in the database
        count = GameImage.objects.filter(difficulty=0).count()
        print(f"Images in test DB: {count}")

        controller = GameController(gamemode=0)
        image_path, location = controller.pick_random_image()
        
        # Check that a result is returned
        self.assertIsNotNone(image_path)
        self.assertIsNotNone(location)
        print(f"Random Image: {image_path}, Location: {location}")

    