from django.test import TestCase
from apps.game.GameController import GameController


class GameControllerTest(TestCase):

    # TC1: Correct answer on first try
    # Expected: 0 attempts, max score
    
    def test_correct_first_try(self):
        controller = GameController("easy")

        # Mock image + answer
        def mock_pick_random_image():
            return ("img.jpg", "Library")

        controller.pick_random_image = mock_pick_random_image

        # Fake input: always correct
        def fake_input(prompt):
            return "Library"

        controller.signalGameStart(input_func=fake_input)

        self.assertEqual(controller.game.getattempts(), 0)
        self.assertEqual(controller.game.getScore(), 3000)
    
    # TC2: Correct answer after 2 wrong attempts
    # Expected: attempts = 2, lower score
    
    def test_correct_after_multiple_attempts(self):
        controller = GameController("easy")

        def mock_pick_random_image():
            return ("img.jpg", "Library")

        controller.pick_random_image = mock_pick_random_image

        inputs = ["Wrong", "Wrong", "Library"]

        def fake_input(prompt):
            return inputs.pop(0)

        controller.signalGameStart(input_func=fake_input)

        self.assertEqual(controller.game.getattempts(), 2)
        self.assertEqual(controller.game.getScore(), 1000)  # (3-2)*1000
    
    # TC3: All incorrect attempts
    # Expected: attempts = 3, score = 0
    
    def test_all_attempts_wrong(self):
        controller = GameController("easy")

        def mock_pick_random_image():
            return ("img.jpg", "Library")

        controller.pick_random_image = mock_pick_random_image

        inputs = ["A", "B", "C"]

        def fake_input(prompt):
            return inputs.pop(0)

        controller.signalGameStart(input_func=fake_input)

        self.assertEqual(controller.game.getattempts(), 3)
        self.assertEqual(controller.game.getScore(), 0)

    # TC4: Hard mode scoring
    # Expected: score doubled
    
    def test_hard_mode_scoring(self):
        controller = GameController(1)  # hard mode in your implementation

        def mock_pick_random_image():
            return ("img.jpg", "Library")

        controller.pick_random_image = mock_pick_random_image

        def fake_input(prompt):
            return "Library"

        controller.signalGameStart(input_func=fake_input)

        self.assertEqual(controller.game.getScore(), 6000)  # (3-0)*2*1000

    # TC5: Stops after correct answer (no extra inputs used)
    
    def test_stops_after_correct(self):
        controller = GameController("easy")

        def mock_pick_random_image():
            return ("img.jpg", "Library")

        controller.pick_random_image = mock_pick_random_image

        inputs = ["Library", "Wrong", "Wrong"]  # only first should be used

        def fake_input(prompt):
            return inputs.pop(0)

        controller.signalGameStart(input_func=fake_input)

        self.assertEqual(controller.game.getattempts(), 0)
        self.assertEqual(len(inputs), 2)  # confirms loop stopped early