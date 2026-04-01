from apps.game import game
from apps.game import image
from apps.game.image import genRandomImage
import random


class GameController:

    def __init__(self, gamemode):
        self.gamemode = gamemode
        self.gameid = random.randint(10000000, 99999999)
        self.game = game(gamemode)

    def pick_random_image(self):
        return genRandomImage(self.gamemode)
    
    def signalGameStart(self):
        image_path, answer = self.pick_random_image(self, self.gamemode)
        self.game.startGame(self.gamemode, image_path, answer)

    

    


    

    