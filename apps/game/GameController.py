from apps.game.GameInstance import GameInstance
from apps.game.Image import genRandomImage
import random


class GameController:

    def __init__(self, gamemode):
        self.gamemode = gamemode
        self.game = GameInstance(gamemode, random.randint(10000000, 99999999))

    def pick_random_image(self):
        return genRandomImage(self.gamemode)

    def signalGameStart(self, input_func=input):
        image_path, answer = self.pick_random_image()

        # Game cycle

        while self.game.getattempts() < 3:
            # Display the Image and prompting text

            # Get user input from input field
            # Use injected input function instead of hardcoded input()
            user_input = input_func(f"Correct Answer is {answer}: ")

            # Replaced gamestart in gameinstance with evaluate to handle game play loop and user input here.
            if self.game.evaluate(user_input, answer):
                # If evaluate returns true, the answer was correct and the score was updated
                break