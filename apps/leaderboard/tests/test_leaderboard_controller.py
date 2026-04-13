from django.test import TestCase
from apps.leaderboard.LeaderboardController import LeaderboardController


# DummyGame
# This is a fake object used ONLY for testing
# It simulates a real game instance without database
#
class DummyGame:

    # Constructor: we create a fake game with score, mode, and ID
    def __init__(self, score, gamemode, game_id):
        self._score = score        # store score
        self.gamemode = gamemode   # store game mode (1, 2, ...)
        self._game_id = game_id    # store game ID

    # this function used by controller to returns score
    def getScore(self):
        return self._score

    # Function used by controller and returns game id
    def getGameID(self):
        return self._game_id


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
        self.controller = LeaderboardController()

    
    # TEST 1: for Get Top Scores (Leaderboard)
    # - to save scores for multiple users
    #  and to check if system returns them sorted, highest - lowest
    # ----------------------------------
    def test_get_top_scores(self):

        # jus fake game results
        game1 = DummyGame(100, 1, 1)   # user1 score  100
        game2 = DummyGame(200, 2, 2)   # user2 score  200
        game3 = DummyGame(150, 1, 3)   # user3 score  150

        # to save scores into leaderboard
        self.controller.save_score("user1", game1)
        self.controller.save_score("user2", game2)
        self.controller.save_score("user3", game3)

        # Retrieve leaderboard should be sorted
        top_scores = self.controller.get_top_scores()

        # print section header to better reading on the console
        print("\n=== Top Scores (Highest → Lowest) ===")

        # to print each leaderboard entry
        for entry in top_scores:
            print(f"User: {entry.user_id} | Score: {entry.score}")

        #  for verifying 

        # Check total number of entries
        self.assertEqual(len(top_scores), 3)

        # Check order the highest score first
        self.assertEqual(top_scores[0].user_id, "user2")
        self.assertEqual(top_scores[0].score, 200)

        self.assertEqual(top_scores[1].user_id, "user3")
        self.assertEqual(top_scores[1].score, 150)

        self.assertEqual(top_scores[2].user_id, "user1")
        self.assertEqual(top_scores[2].score, 100)

    
    ##### now  TEST 2 Get Scores for One User
    
    #     Save multiple scores for SAME user
    # and  check if system returns ALL scores for that user


    def test_get_user_scores(self):

        # game results
        game1 = DummyGame(100, 1, 1)   # 1 game
        game2 = DummyGame(200, 2, 2)   # 2nd game

        # Save both scores for the same user
        self.controller.save_score("user1", game1)
        self.controller.save_score("user1", game2)

        # Retrieve scores ONLY for user1
        user_scores = self.controller.get_user_scores("user1")

        # Print header
        print("\n=== Scores for user1 ===")

        # Print all results
        for entry in user_scores:
            print(f"User: {entry.user_id} | Score: {entry.score}")

        # ## Assertions 
        # Check total entries for user1
        self.assertEqual(len(user_scores), 2)

        # Check both belong to user1
        self.assertEqual(user_scores[0].user_id, "user1")
        self.assertEqual(user_scores[1].user_id, "user1")




# #####
    # TEST 3     Empty Leaderboard
    # to check the behavior when no scores exist
    # the System should not crash
    # and should return empty list
    # ------------------------------------------
    def test_empty_leaderboard(self):

        # get leaderboard when database is empty
        top_scores = self.controller.get_top_scores()

        # Print  header on console
        print("\n=== Empty Leaderboard ===")

        #  to print result
        if not top_scores:
            print("No scores available.")
        else:
            for entry in top_scores:
                print(f"User: {entry.user_id} | Score: {entry.score}")

        # verify

        # Expect no results
        self.assertEqual(len(top_scores), 0)






        # to run the test 

       # Activate environment
       #.venv\Scripts\activate

       # Make sure you are in project root (where manage.py is)

       # run the cmd
        #python manage.py test apps.leaderboard.tests.test_leaderboard_controller --verbosity=0