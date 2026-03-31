from apps.game import Game
from apps.game import Image
from apps.game.Image import genRandomImage
import random


class GameController:

    def __init__(self, gamemode):
        self.gamemode = gamemode
        self.gameid = random.randint(10000000, 99999999)
        self.game = Game(gamemode)
    
    def signalGameStart(self):
        self.startGame()

    def pick_random_image(self):
        return genRandomImage(self.gamemode)

    


    

    