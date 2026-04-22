from apps.game.GameInstance import GameInstance
from apps.game.models import GameResult
from apps.game.Image import genRandomImage
import random


class GameController:

    def __init__(self, gamemode, user_id):
        self.gamemode = gamemode
        self.user_id = user_id
        self.game = GameInstance(gamemode)

    def pick_random_image(self):
        return genRandomImage(self.gamemode)

    # Added answer parameter to allow web-based guess verification
    def GameStart(self, input_func=input, answer=None):
        if answer is None:
            image_path, answer = self.pick_random_image()

        # Game cycle

        while self.game.getattempts() < 3:
            # Display the Image and prompting text

            # Get user input from input field
            # Use injected input function instead of hardcoded input()
            user_input = input_func(f"Correct Answer is {answer}: ")

            # Replaced gamestart in gameinstance with evaluate to handle game play loop and user input here.
            try:
                if self.game.evaluate(user_input, answer):
                    # If evaluate returns true, the answer was correct and the score was updated
                    break
            except ValueError:
                print("Error: Invalid game mode")
                break
        
        # Return result so it can be saved by the view
        return GameResult(user_id_id=self.user_id, score=self.game.getScore(), gamemode=self.gamemode)