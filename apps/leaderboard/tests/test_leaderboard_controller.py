from django.test import TestCase
from apps.leaderboard.LeaderboardController import LeaderboardController
from apps.accounts.models import User

# ---------------------
# DummyGame
# Used to simulate a game instance for isolated testing
# ---------------------
class DummyGame:
    def __init__(self, score, gamemode, game_id):
        self._score = score
        self.gamemode = gamemode
        self._game_id = game_id

    def getScore(self):
        return self._score

    def getGameID(self):
        return self._game_id


# ---------------------------------------------------
# Test Class for LeaderboardController
# ---------------------------------------------------
class TestLeaderboardController(TestCase):

    def setUp(self):
        """Runs BEFORE every test: creates a fresh controller and test users."""
        self.controller = LeaderboardController()
        
        # Create real users in the test database to satisfy Foreign Key requirements
        self.user1 = User.objects.create(
            userName="UserOne", 
            userEmail="user1@utdallas.edu", 
            userPassword="password12345"
        )
        self.user2 = User.objects.create(
            userName="UserTwo", 
            userEmail="user2@utdallas.edu", 
            userPassword="password12345"
        )
        self.user3 = User.objects.create(
            userName="UserThree", 
            userEmail="user3@utdallas.edu", 
            userPassword="password12345"
        )

    def test_get_top_scores(self):
        """TEST 1: Verify scores are returned sorted Highest -> Lowest."""
        game1 = DummyGame(100, 1, 1)  # UserOne score 100
        game2 = DummyGame(200, 2, 2)  # UserTwo score 200
        game3 = DummyGame(150, 1, 3)  # UserThree score 150

        # Save scores using the real userId from the database
        self.controller.save_score(self.user1.userId, game1)
        self.controller.save_score(self.user2.userId, game2)
        self.controller.save_score(self.user3.userId, game3)

        # Retrieve sorted leaderboard
        top_scores = self.controller.get_top_scores()

        print("\n=== Top Scores (Highest → Lowest) ===")
        for entry in top_scores:
            # Note: access user via the relationship 'user.userName'
            print(f"User: {entry.user.userName} | Score: {entry.score}")

        # Assertions
        self.assertEqual(len(top_scores), 3)

        # Verify correct sorting (highest first)
        self.assertEqual(top_scores[0].user.userName, "UserTwo")
        self.assertEqual(top_scores[0].score, 200)

        self.assertEqual(top_scores[1].user.userName, "UserThree")
        self.assertEqual(top_scores[1].score, 150)

        self.assertEqual(top_scores[2].user.userName, "UserOne")
        self.assertEqual(top_scores[2].score, 100)

    def test_get_user_scores(self):
        """TEST 2: Verify all scores for a SPECIFIC user can be retrieved."""
        game1 = DummyGame(120, 1, 10)
        game2 = DummyGame(250, 2, 11)

        # Save two different scores for UserOne
        self.controller.save_score(self.user1.userId, game1)
        self.controller.save_score(self.user1.userId, game2)

        # Retrieve scores ONLY for user1
        user_scores = self.controller.get_user_scores(self.user1.userId)

        print(f"\n=== Scores for {self.user1.userName} ===")
        for entry in user_scores:
            print(f"User: {entry.user.userName} | Score: {entry.score}")

        # Assertions
        self.assertEqual(len(user_scores), 2)
        self.assertEqual(user_scores[0].user.userId, self.user1.userId)
        self.assertEqual(user_scores[1].user.userId, self.user1.userId)

    def test_empty_leaderboard(self):
        """TEST 3: Verify system returns empty list instead of crashing if no scores exist."""
        top_scores = self.controller.get_top_scores()

        print("\n=== Empty Leaderboard ===")
        if not top_scores:
            print("No scores available.")

        # Assertions
        self.assertEqual(len(top_scores), 0)