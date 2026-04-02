from apps.game.GameInstance import GameInstance
from apps.game.Image import genRandomImage
import random


class GameController:

    def init(self, gamemode):
        self.gamemode = gamemode
        self.game = GameInstance(gamemode, random.randint(10000000, 99999999))

    def pick_random_image(self):
        return genRandomImage(self.gamemode)

    def signalGameStart(self):
        image_path, answer = self.pick_random_image(self, self.gamemode)

        # Game cycle

        while self.game.getattempts < 3: 
            # Display the Image and propting text

            # Get user input from input field
            user_input = input("Correct Answer is {answer}: ") # Temporary, will need to get from Django

            # Replaced gamestart in gameinstance with evaluate to handle game play loop and user input here.
            if (self.game.evaluate(user_input, answer)): 
                # If evaluate returns true, the answer was correct and the score was updated
                break