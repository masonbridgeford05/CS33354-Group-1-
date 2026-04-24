


from django.test import TestCase

from apps.accounts.models import User
from apps.game.models import GameResult
from apps.leaderboard.LeaderboardController import LeaderboardController


class TestLeaderboardController(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(userName="alice", userEmail="alice@test.com", userPassword="pass123")
        self.user2 = User.objects.create(userName="bob", userEmail="bob@test.com", userPassword="pass456")
        self.user3 = User.objects.create(userName="charlie", userEmail="charlie@test.com", userPassword="pass789")

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
        print("Running: check leaderboard returns exactly 10 results - success")
        top_scores = self.controller.get_top_scores()
        self.assertEqual(len(top_scores), 10)

    def test_get_top_scores_highest_score_first(self):
        print("Running: check highest score is first - success")
        top_scores = self.controller.get_top_scores()
        self.assertEqual(top_scores[0].score, 9500)

    def test_get_top_scores_sorted_descending(self):
        print("Running: check scores sorted descending - success")
        top_scores = self.controller.get_top_scores()

        for i in range(len(top_scores) - 1):
            self.assertGreaterEqual(top_scores[i].score, top_scores[i + 1].score)

    def test_get_top_scores_includes_only_top_10_scores(self):
        print("Running: check exact top 10 scores list - success")
        top_scores = self.controller.get_top_scores()
        scores = [game.score for game in top_scores]

        expected_scores = [9500, 9500, 9200, 9100, 8800, 8400, 8100, 7800, 7600, 7200]

        self.assertEqual(scores, expected_scores)

    def test_get_top_scores_lowest_score_in_top_10(self):
        print("Running: check lowest score in top 10 is 7200")
        top_scores = self.controller.get_top_scores()
        self.assertEqual(top_scores[9].score, 7200)








# .venv\Scripts\Activate.ps1
# python manage.py test apps.leaderboard.tests.leaderboard-tests

