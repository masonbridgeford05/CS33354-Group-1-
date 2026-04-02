from django.test import TestCase
from apps.game.Image import GameImage
from apps.game.GameController import GameController
from apps.game.GameInstance import GameInstance


class GameInstanceTest(TestCase):

    # TC1: Valid guess, valid location
    # Expected: True, score calculated
    
    def test_correct_guess_easy(self):
        game = GameInstance("easy", 1)

        result = game.evaluate("Library", "Library")

        self.assertTrue(result)
        self.assertEqual(game.getScore(), 3000)  # (3-0)*1000

    # TC2: Incorrect guess increments attempts
    # Expected: False, attempts + 1
    
    def test_incorrect_guess_increments_attempts(self):
        game = GameInstance("easy", 1)

        result = game.evaluate("ECSW", "Library")

        self.assertFalse(result)
        self.assertEqual(game.getattempts(), 1)
    
    # TC3: Multiple incorrect guesses
    # Expected: attempts increment properly
    
    def test_multiple_incorrect_attempts(self):
        game = GameInstance("easy", 1)

        game.evaluate("A", "B")
        game.evaluate("C", "B")
        game.evaluate("D", "B")

        self.assertEqual(game.getattempts(), 3)
    
    # TC4: Correct guess after some attempts
    # Expected: score reflects attempts
    
    def test_correct_after_attempts(self):
        game = GameInstance("easy", 1)

        game.evaluate("A", "B")  # attempt 1
        game.evaluate("B", "B")  # correct

        self.assertTrue(game.evaluate("B", "B"))
        # attempts = 1 → score = (3-1)*1000 = 2000
        self.assertEqual(game.getScore(), 2000)

    # TC5: Score calculation (Easy)
    
    def test_calculate_score_easy(self):
        game = GameInstance("easy", 1)

        game.attempts = 2
        game.calculateScore()

        self.assertEqual(game.getScore(), 1000)  # (3-2)*1000
    
    # TC6: Score calculation Hard (gamemode == 1)
    
    def test_calculate_score_hard(self):
        game = GameInstance(1, 1)  # hard mode

        game.attempts = 1
        game.calculateScore()

        self.assertEqual(game.getScore(), 4000)  # (3-1)*2*1000

    # TC7: incrementAttempts method
    
    def test_increment_attempts(self):
        game = GameInstance("easy", 1)

        game.incrementAttempts()
        game.incrementAttempts()

        self.assertEqual(game.getattempts(), 2)

    # TC8: getGameID method
    
    def test_get_game_id(self):
        game = GameInstance("easy", 12345)

        self.assertEqual(game.getGameID(), 12345)
    
    # TC9: Edge case - wrong inputs still handled
    # Expected to return False
    
    def test_invalid_location_input(self):
        game = GameInstance("easy", 1)

        result = game.evaluate("InvalidPlace", "Library")

        self.assertFalse(result)
        self.assertEqual(game.getattempts(), 1)

    # TC10: Empty input case
    
    def test_empty_input(self):
        game = GameInstance("easy", 1)

        result = game.evaluate("", "Library")

        self.assertFalse(result)
        self.assertEqual(game.getattempts(), 1)
