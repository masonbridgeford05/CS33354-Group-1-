from django.test import TestCase
from apps.game.GameInstance import GameInstance

class GameInstanceTest(TestCase):

    # TC1: Valid location, valid difficulty
    # Expected: True, score calculated
    
    def test_correct_guess_easy(self):
        print("\nTC1 Input: difficulty='easy', location='Library' Expected: True, score=3000")
        game = GameInstance("easy", 1)

        result = game.evaluate("Library", "Library")

        self.assertTrue(result)
        self.assertEqual(game.getScore(), 3000)  # (3-0)*1000
        print("TC1 Passed")

    # TC2: Invalid location, valid difficulty

    def test_invalid_location(self):
        print("\nTC2 Input: difficulty='hard', location='Bank' Expected: False")
        game = GameInstance("hard", 1)

        result = game.evaluate("Bank", "Library")

        self.assertFalse(result)
        print("TC2 Passed")

    # TC3: Exceptional Location Input (empty string), valid difficulty
    
    def test_empty_input(self):
        print("\nTC3 Input: difficulty='easy', location='' Expected: False, attempts+1")
        game = GameInstance("easy", 1)

        result = game.evaluate("", "Library")

        self.assertFalse(result)
        self.assertEqual(game.getattempts(), 1)
        print("TC3 Passed")

    # TC4: Invalid difficulty, valid location
    
    def test_invalid_difficulty(self):
        print("\nTC4 Input: difficulty='impossible', location='ECSN' Expected: ValueError")
        game = GameInstance("impossible", 1)

        with self.assertRaises(ValueError):
            game.evaluate("Library", "Library")

        print("TC4 Passed")

    # TC7: Null difficulty, valid location
    
    def test_null_difficulty(self):
        print("\nTC7 Input: difficulty=None, location='Dining Hall' Expected: ValueError")
        game = GameInstance(None, 1)

        with self.assertRaises(ValueError):
            game.evaluate("Dining Hall", "Dining Hall")

        print("TC7 Passed")

    # TC5: Incorrect guess increments attempts
    # Expected: False, attempts + 1
    
    def test_incorrect_guess_increments_attempts(self):
        print("\nTC5 Input: difficulty='easy', location='ECSW' Expected: False, attempts=1")
        game = GameInstance("easy", 1)

        result = game.evaluate("ECSW", "Library")

        self.assertFalse(result)
        self.assertEqual(game.getattempts(), 1)
        print("TC5 Passed")
    
    # TC6: Multiple incorrect guesses
    # Expected: attempts increment properly
    
    def test_multiple_incorrect_attempts(self):
        print("\nTC6 Input: multiple incorrect guesses Expected: attempts=3")
        game = GameInstance("easy", 1)

        game.evaluate("A", "B")
        game.evaluate("C", "B")
        game.evaluate("D", "B")

        self.assertEqual(game.getattempts(), 3)
        print("TC6 Passed")
    
    # TC8: Correct guess after some attempts
    # Expected: score reflects attempts
    
    def test_correct_after_attempts(self):
        print("\nTC8 Input: correct after wrong attempts Expected: True, score=2000")
        game = GameInstance("easy", 1)

        game.evaluate("A", "B")  # attempt 1
        game.evaluate("B", "B")  # correct

        self.assertTrue(game.evaluate("B", "B"))
        # attempts = 1 → score = (3-1)*1000 = 2000
        self.assertEqual(game.getScore(), 2000)
        print("TC8 Passed")

    # TC9: Score calculation (on easy mode)
    
    def test_calculate_score_easy(self):
        print("\nTC9 Input: attempts=2, easy mode Expected: score=1000")
        game = GameInstance("easy", 1)

        game.attempts = 2
        game.calculateScore()

        self.assertEqual(game.getScore(), 1000)  # (3-2)*1000
        print("TC9 Passed")
    
    # TC10: Score calculation Hard (gamemode == 1)
    
    def test_calculate_score_hard(self):
        print("\nTC10 Input: attempts=1, hard mode Expected: score=4000")
        game = GameInstance(1, 1)  # hard mode

        game.attempts = 1
        game.calculateScore()

        self.assertEqual(game.getScore(), 4000)  # (3-1)*2*1000
        print("TC10 Passed")

    # TC11: incrementAttempts method
    
    def test_increment_attempts(self):
        print("\nTC11 Input: increment attempts twice Expected: attempts=2")
        game = GameInstance("easy", 1)

        game.incrementAttempts()
        game.incrementAttempts()

        self.assertEqual(game.getattempts(), 2)
        print("TC11 Passed")

    # TC12: getGameID method
    
    def test_get_game_id(self):
        print("\nTC12 Input: gameID=12345 Expected: 12345")
        game = GameInstance("easy", 12345)

        self.assertEqual(game.getGameID(), 12345)
        print("TC12 Passed")
    