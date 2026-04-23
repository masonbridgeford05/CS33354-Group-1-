from django.test import TestCase
from django.contrib.auth.models import User
from apps.game.models import GameResult
from apps.leaderboard.LeaderboardController import LeaderboardController


# ---------------------
# creating the Test Class for LeaderboardController
# and Django will run this class automatically
# ---------------------------------------------------
class TestLeaderboardController(TestCase):

    
    # setUp()
    # Runs BEFORE every test
    # and creates a fresh controller each time
    # ------------------------------------
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="pass123")
        self.user2 = User.objects.create_user(username="bob", password="pass456")
        self.user3 = User.objects.create_user(username="charlie", password="pass789")

        game_data = [
            (1,  self.user1, 9500, True),
            (2,  self.user2, 7200, False),
            (3,  self.user3, 8800, True),
            (4,  self.user1, 3100, False),
            (5,  self.user2, 9500, True),
            (6,  self.user3, 6700, False),
            (7,  self.user1, 4400, True),
            (8,  self.user2, 8100, False),
            (9,  self.user3, 2200, True),
            (10, self.user1, 7800, False),
            (11, self.user2, 5500, True),
            (12, self.user3, 9100, False),
            (13, self.user1, 1300, True),
            (14, self.user2, 6300, False),
            (15, self.user3, 8400, True),
            (16, self.user1, 4900, False),
            (17, self.user2, 3700, True),
            (18, self.user3, 7600, False),
            (19, self.user1, 9200, True),
            (20, self.user2, 5100, False),
        ]

        for game_result_id, user, score, difficult in game_data:
            GameResult.objects.create(
                game_result_id=game_result_id,
                user_id=user,
                score=score,
                difficult=difficult
            )

        self.controller = LeaderboardController()

    def test_get_top_scores_returns_10(self):
        top_scores = self.controller.get_top_scores()
        self.assertEqual(len(top_scores), 10)

    
    